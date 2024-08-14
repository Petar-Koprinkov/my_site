from django.shortcuts import render, get_object_or_404

from my_site.blog.models import Post, Author


def index(request):
    posts = Post.objects.select_related("author").order_by("-date")[:3]
    author = Author.objects.get(last_name='Koprinkov')
    context = {
        "posts": posts,
        "author": author,
    }

    return render(request, 'blog/index.html', context)


def blog_page(request):
    posts = Post.objects.select_related("author")
    context = {
        "posts": posts,
    }

    return render(request, 'blog/all-post.html', context)


def blog_detail_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    contex = {
        "post": post,
    }
    return render(request, 'blog/post-details.html', contex)
