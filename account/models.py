from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    #validator for phone number
    mobile_validation = RegexValidator (regex='(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}',code="invalid",message='phone number most be entered in the format 09999999999')
    age = models.PositiveIntegerField(blank=True,null=True)
    bio = models.TextField(max_length=200,blank=True)
    profile = models.ImageField(blank = True,upload_to = 'user/profile/')
    phone_number = models.CharField(max_length=11,validators=[mobile_validation],null=True)
    is_premium_account = models.BooleanField(default=False)
    last_profile_updated = models.DateTimeField(auto_now=True)
    blocked_users = models.ManyToManyField('self', blank=True)

    def legal_age(self):
        if self.age <= 18 :
            return  False
        else:
            return  True

    def is_can_update(self):
        if self.last_profile_updated > timezone.now():
            return True
        else:
            return False
    is_can_update.boolean = True


    def blocked_users_to_str(self):
        return ", ".join([blocked.username for blocked in self.blocked_users.all()])
        



class BlockAndReportModel(models.Model):

    reporter = models.ForeignKey(User,null=True,on_delete= models.CASCADE,related_name='reporter')
    reported = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='user_report')
    report_on_post = models.ForeignKey("Post.PostModel",null=True,on_delete=models.CASCADE,related_name='post_reported')
    report_text = models.CharField(max_length=400,blank=True)
    number_reported = models.PositiveSmallIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.reported} - {self.report_text}"



class RelationFollowingModel(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.from_user} followed {self.to_user}"



