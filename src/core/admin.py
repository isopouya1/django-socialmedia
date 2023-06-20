from django.contrib import admin
from core.models import Profile , Post , Like ,Comment
# Register your models here.

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','Image']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Like)


admin.site.register(Comment)
