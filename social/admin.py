from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Post

# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Profile

admin.site.unregister(Group)
class UserAdmin(admin.ModelAdmin):
    model=User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(Post)
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)