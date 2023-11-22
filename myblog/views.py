from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import postForm
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

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





# Create your views here.
