from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Additional Info',{'fields':('date_of_birth','profile_photo')}),
                                       )
    add_fieldsets = UserAdmin.add_fieldsets + (('Additional Info', {'fields': ('date_of_birth','profile_photo')}),
                                               )
    
    admin.site.register(CustomUser,CustomUserAdmin)

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
#Import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass 
admin.site.register(CustomUser,CustomUserAdmin)

