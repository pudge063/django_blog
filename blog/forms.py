from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему поста',
                'required': True,
                'id': 'create_post_title'                      
        }),

            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст поста',
                'required': True,
                'id': 'create_post_content',
            }),
        }
        labels = {
            'title': '',
            'text': '',
        }