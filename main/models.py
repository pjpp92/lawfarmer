from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = HTMLField()
    score = models.IntegerField()
    thema = models.ForeignKey('Tag')
    data = models.DateTimeField(auto_now_add=True)

    def  __unicode__(self):
        return u'%s %s' % (self.thema.title, self.title)

class Comment(models.Model):
    author_name = models.CharField(max_length=3000)
    content = models.TextField()
    post = models.ForeignKey('Post')
    data = models.DateTimeField(auto_now_add=True)