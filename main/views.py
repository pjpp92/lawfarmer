from django.shortcuts import render, redirect
from .models import Tag, Post, Comment

# Create your views here.
def home(request):
    v = dict()
    tag = request.GET.get('tag', '')
    if tag:
        try:
            tag = Tag.objects.get(title=tag)
            v['posts'] = Post.objects.filter(thema=tag)
        except:
            pass
    else:
        v['posts'] = Post.objects.all()
    v['tags'] = Tag.objects.all()
    v['top_posts'] = Post.objects.all().order_by('score')
    return render(request, 'index.html', v)


def article(request):
    slug = request.GET.get('id', '')
    if slug:
        try:
            v = dict()
            v['tags'] = Tag.objects.all()
            v['top_posts'] = Post.objects.all().order_by('score')
            v['post'] = Post.objects.get(pk=int(slug))
            return render(request, 'article.html', v)
        except:
            return redirect('home')
    else:
        return redirect('home')


def flatblock(request, block):
    v = dict()
    v['tags'] = Tag.objects.all()
    v['text'] = block
    v['top_posts'] = Post.objects.all().order_by('score')
    return render(request, 'block.html', v)