from django import forms

from my_site.blog.models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'username': 'Your Name',
            'email': 'Your Email',
            'text': 'Your Comment',
        }


class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search for post...'}),
        required=False,
    )