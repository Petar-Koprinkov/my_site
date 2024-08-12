from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def blog_page(request):
    return render(request, 'blog/all-post.html')


def blog_detail_page(request):
    pass
