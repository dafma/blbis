from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def detail(request, slug, *args, **kwargs):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        'object': obj,
    }
    return render(request, 'blog/detail.html', context)


def indexblog(request, *args, **kwargs):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, 'blog/blog.html', context)