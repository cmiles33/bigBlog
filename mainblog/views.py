from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm, PostForm
import re
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'mainblog/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # Get list of active comments
    comments = post.comments.filter(active=True)

    # Comment form section of a post

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'mainblog/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})

@login_required
def create_post(request):
    print(request.user.username)
    new_post = None
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            slug_title = str(new_post.title).lstrip().rstrip().replace(" ","-")
            # Save post information
            new_post.slug = slug_title
            new_post.author = request.user
            new_post.status = "published"
            new_post.save()
    else:
        post_form = PostForm()

    return render(request,
                  'mainblog/create_post.html',
                  {'post_form': post_form,
                   'new_post': new_post,})

@login_required
def view_profile(request):
    print(request.user.username)
    posts = Post.objects.filter(author=request.user)

    return render(request,
                  'mainblog/profile.html',
                  {'posts': posts,
                   })

