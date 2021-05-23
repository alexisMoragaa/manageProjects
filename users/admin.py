#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


# Local
from users.models import Profile
from django.contrib.auth.models import User



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
