from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Tag, Post, Comment

# Create your views here.
def home(request):
    v = dict()
    tag = request.GET.get('tags', '')
    page = request.GET.get('page')
    if tag:
        try:
            tag = Tag.objects.get(title=tag)
            posts = Post.objects.filter(thema__title=tag)
        except:
            posts = Post.objects.all()
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 1)
    try:
        v['posts'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        v['posts'] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        v['posts'] = paginator.page(paginator.num_pages)

    v['tags'] = Tag.objects.all()
    v['top_posts'] = Post.objects.all().order_by('score')
    v['tag_url'] = tag
    return render(request, 'index.html', v)


def article(request):
    slug = request.GET.get('id', '')
    if slug:


            v = dict()
            v['tags'] = Tag.objects.all()
            v['top_posts'] = Post.objects.all().order_by('score')
            v['post'] = Post.objects.get(pk=int(slug))
            print slug
            if request.method == 'POST':
                print request.POST['author_email']
                c = Comment.objects.create(content=request.POST['content'], author_email=request.POST['author_email'], post=v['post'])
                c.save()
            v['comments'] = Comment.objects.filter(post=v['post'])
            return render(request, 'article.html', v)

    else:
        return redirect('home')


def flatblock(request, block):
    v = dict()
    v['tags'] = Tag.objects.all()
    v['text'] = block
    v['top_posts'] = Post.objects.all().order_by('score')
    return render(request, 'block.html', v)


