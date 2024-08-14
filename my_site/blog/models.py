from django.db import models
from django.template.defaultfilters import slugify


class Author(models.Model):
    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(
        max_length=50
    )
    excerpt = models.TextField()

    image_name = models.CharField(
        max_length=50
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    slug = models.SlugField(
        unique=True,
    )

    content = models.TextField()

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    caption = models.CharField(
        max_length=50
    )

    posts = models.ManyToManyField(
        to=Post,
        related_name='tags'
    )
