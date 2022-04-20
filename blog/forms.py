from django import forms
from blog.models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author', 'title', 'image', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass', 'placeholder':'Title'}),
            'text':forms.Textarea(attrs={'class':'editable form-control postcontent'}),
        }


class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your comment here'}))


    class Meta():
        model = Comment
        fields = ('author', 'text')


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
