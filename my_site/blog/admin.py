from django.contrib import admin

from .models import Author, Post, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author__last_name', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)