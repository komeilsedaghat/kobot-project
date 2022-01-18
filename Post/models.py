from email.mime import image
from pyexpat import model
from xml.dom import ValidationErr
from django.db import models
from django.db.models.base import Model
from account.models import User

# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to = 'image/',blank = True)
    video = models.FileField(upload_to='video/',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status  = models.BooleanField(default=True)
    views = models.ManyToManyField('IPAddress',blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} - {self.text}"

    def save(self, *args, **kwargs):
        if self.image and self.video:
            raise ValidationErr("you can't upload video and photo in one post please upload one of them")

        super(PostModel, self).save()


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class CommentsModel(models.Model):
    post = models.ForeignKey(PostModel,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f"{self.user} - {self.comment}"

        
class LikeModel(models.Model):
    from_like = models.ForeignKey(User,on_delete= models.CASCADE,related_name= 'liker')
    to_like = models.ForeignKey(User,on_delete  = models.CASCADE,related_name= 'liked')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.from_like} liked {self.to_like}"