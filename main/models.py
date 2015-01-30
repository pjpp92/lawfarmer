from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=30)

    def  __unicode__(self):
        return u'%s' % (self.title)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = HTMLField()
    score = models.IntegerField()
    thema = models.ManyToManyField(Tag)
    data = models.DateTimeField(auto_now_add=True)

    def  __unicode__(self):
        return u'%s' % (self.title)

class Comment(models.Model):
    author_email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey('Post')
    data = models.DateTimeField(auto_now_add=True)

    def  __unicode__(self):
        return u'%s %s' % (self.content, self.data)