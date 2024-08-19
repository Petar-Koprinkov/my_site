from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View

from my_site.blog.forms import CommentsForm
from my_site.blog.models import Post


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        query = super().get_queryset()
        data = query[0:3]
        return data


class BlogPageView(ListView):
    model = Post
    template_name = 'blog/all-post.html'
    context_object_name = 'posts'
    ordering = ['-date']


class BlogDetailPageView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentsForm()
        context = {
            'form': form,
            'post': post,
            'comments': post.comments.order_by('-date'),
            }
        return render(request, 'blog/post-details.html', context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_detail_page', slug=slug)

        form = CommentsForm(request.POST)
        context = {
            'form': form,
            'post': post,
            'comments': post.comments.order_by('-date'),
        }
        return render(request, 'blog/post-details.html', context)

