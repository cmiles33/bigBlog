from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, CategoryData
from .forms import CommentForm, PostForm
import re
import re
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'mainblog/list.html',
                  {'posts': posts})


def view_categories(request):
    categories = CategoryData.objects.filter(hidden=False)

    return render(request,
                  'mainblog/categoryList.html',
                  {'categories': categories,
                   })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    print(post.id)
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
            slug_title = str(new_post.title)
            slug_title = slug_title.split(" ")
            newtitle = []
            for words in slug_title:
                newtitle.append(re.sub(r'[\W_]+','',words))
            newslug = "-".join(newtitle)
            print(newslug)
            # Save post information
            new_post.slug = newslug
            new_post.author = request.user
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
    posts = Post.objects.filter(author=request.user,
                                status="published")
    drafted_posts = Post.objects.filter(status="draft",
                                        author=request.user)

    return render(request,
                  'mainblog/profile.html',
                  {'posts': posts,
                   'post_drafts': drafted_posts,
                   })

@login_required
def view_post_drafts(request,post_id):
    # There needs to be a check to make
    # sure only the author can edit there post
    # This is also used to EDIT published posts.
    print("loading drafts")
    draftPost = get_object_or_404(Post, id=post_id)
    if draftPost.author.username != request.user.username:
        return redirect('mainblog:post_list')

    finished = False
    draftForm = PostForm(instance=draftPost)
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            update_post = post_form.save(commit=False)

            new_post = Post.objects.get(id=post_id)

            slug_title = str(update_post.title)
            slug_title = slug_title.split(" ")
            newtitle = []
            for words in slug_title:
                newtitle.append(re.sub(r'[\W_]+','',words))
            newslug = "-".join(newtitle)
            print(newslug)
            # Save post information
            new_post.title = update_post.title
            new_post.slug = newslug
            new_post.body = update_post.body
            new_post.category = update_post.category
            new_post.status = update_post.status
            new_post.save()
            finished = True

    return render(request,'mainblog/draft_view.html',
                  {'draftForm': draftForm,
                   'finished': finished})


