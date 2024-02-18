from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import postForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

@login_required
def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user==post.author:
        post.delete()
        print("Deleted")
    return redirect('post_list')

@login_required
def post_new(request):
    if request.method == "POST":
         form = postForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
    else:
        form=postForm()
    return render(request, 'myblog/post_edit.html', {'form':form})


def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'myblog/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'myblog/register.html', {'form': form})



# Create your views here.
