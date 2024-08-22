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

    def is_post_stored(self, request, post_id):
        stored_post = request.session.get('stored_post')
        if stored_post is not None:
            is_saved = post_id in stored_post
        else:
            is_saved = False
        return is_saved

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentsForm()

        context = {
            'form': form,
            'post': post,
            'comments': post.comments.order_by('-date'),
            'is_saved': self.is_post_stored(request, post.id),
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
            'is_saved': self.is_post_stored(request, post.id),
        }
        return render(request, 'blog/post-details.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get('stored_post')
        context = {}

        if stored_post is None:
            context['posts'] = []
            context['has_posts'] = False
        else:
            post = Post.objects.filter(id__in=stored_post)
            context['has_posts'] = True
            context['posts'] = post

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_post = request.session.get('stored_post')

        if stored_post is None or len(stored_post) == 0:
            stored_post = []

        post_id = int(request.POST.get('post_id'))

        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)
        request.session['stored_post'] = stored_post

        return redirect('blog_page')

