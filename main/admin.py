from django.contrib import admin

# Register your models here.
from .models import Tag, Post, Comment

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)