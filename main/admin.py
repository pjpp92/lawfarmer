from django.contrib import admin

from .models import Tag, Post, Comment

from mce_filebrowser.admin import MCEFilebrowserAdmin

class PostAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
