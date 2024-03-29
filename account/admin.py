from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,BlockAndReportModel,RelationFollowingModel



UserAdmin.fieldsets[2][1]['fields'] = (
                                'is_active',
                                'is_staff',
                                'is_superuser',
                                'is_premium_account',
                                'age',
                                'bio',
                                'profile',
                                'phone_number',
                                'blocked_users',
                                'groups',
                                'user_permissions',
                                  )

admin.site.register(User,UserAdmin)
admin.site.register(BlockAndReportModel)
admin.site.register(RelationFollowingModel)