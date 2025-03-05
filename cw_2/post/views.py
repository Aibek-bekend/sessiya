from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# 1. GET - Барлық посттарды алу
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

# 2. GET - Белгілі бір постты алу
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'posts': post})

# 3. POST - Жаңа пост қосу
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

# 4. DELETE - Постты өшіру
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')


from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")  # Сіздің URL атауыңызға сәйкес ауыстырыңыз
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {"form": form})
