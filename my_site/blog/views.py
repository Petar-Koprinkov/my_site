from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from my_site.blog.models import Post, Author


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


class BlogDetailPageView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context


