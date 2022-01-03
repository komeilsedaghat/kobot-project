from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,BlockAndReportModel



UserAdmin.fieldsets[2][1]['fields'] = (
                                'is_active',
                                'is_staff',
                                'is_superuser',
                                'is_premium_account',
                                'age',
                                'phone_number',
                                'blocked_users',
                                'groups',
                                'user_permissions',
                                  )

admin.site.register(User,UserAdmin)
admin.site.register(BlockAndReportModel)