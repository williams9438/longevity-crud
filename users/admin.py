from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'image',)}),
        ('Contact info', {'fields': ('email', 'mobile_phone')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Login Info', {'fields': ('username', 'password')}),
    )
    list_display = ['email', 'username', 'is_active',]
    list_filter = ('is_staff', 'is_superuser', 'is_active',)



admin.site.register(User, UserAdmin)