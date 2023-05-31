from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'date']

        widgets = {
            "title": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Название Поста'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст Поста'
            }),
        }