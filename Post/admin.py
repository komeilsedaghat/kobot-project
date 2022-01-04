from django.contrib import admin
from .models import PostModel,IPAddress,CommentsModel
# Register your models here.


admin.site.register(PostModel)
admin.site.register(IPAddress)
admin.site.register(CommentsModel)