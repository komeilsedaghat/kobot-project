from django.db import models
from django.db.models.base import Model
from account.models import User

# Create your models here.

class PostModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status  = models.BooleanField(default=True)
    views = models.ManyToManyField('IPAddress',blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} - {self.text}"



class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class CommentsModel(models.Model):
    post = models.ForeignKey(PostModel,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.comment}"