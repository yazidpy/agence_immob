from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
@admin.register(models.User)
class AdminUser(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    ) 
    list_display = ['first_name', 'last_name', 'email', 'username']
    # # list_editable=['user_type']
    # # ordering=['first_name']
    # # list_per_page=10
    # # search_fields=['first_name','last_name']
    # # list_filter=['user_type']
    

