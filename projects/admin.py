#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


#Moedels 
from projects.models import Card, Column, Profile, Project
from django.contrib.auth.models import User


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """config options for show in admin view"""
    list_display = ('pk', 'name','created_at', 'updated_at')
    list_display_links = ('pk', 'name', 'created_at', 'updated_at')
    search_fields = ('pk','name','user__user__username')


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created_at', 'updated_at')
    list_display_links = ('pk', 'name','created_at', 'updated_at')
    search_fields = ('project__name', 'name', 'pk', 'user__user__username')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at')
    list_display_links = ('pk', 'title', 'created_at', 'updated_at')
    search_fields = ('pk', 'title', 'column__name', 'column__project__name', 'user__user__username')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'number',  'picture', 'created_at', 'updated_at')
    list_display_links = ('pk', 'user','number', 'created_at', 'updated_at')
    search_fields = ('user__username', 'number')





class ProfileInline(admin.StackedInline):
    """Config inline profile for show profile in admin user view"""
    model = Profile
    can_delete =  False
    verbose_name_plural = 'Profiles'


class UserAdnin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
"""Unregister model user, this model be unregister for register with the model profile using tupla userAdmin"""
admin.site.register(User, UserAdnin)
"""in this sentence register model user again using the tupla UserAdin to leave then together"""
