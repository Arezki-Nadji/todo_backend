from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_mangement.models import TodoUserProfile
from django.contrib.auth.models import User

class TodoUserProfileInline(admin.StackedInline):

    model = TodoUserProfile

class TodoUserAdmin(UserAdmin):

    inlines = (TodoUserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)