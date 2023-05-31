from .models import Comment
from django import forms
from django.contrib.auth import authenticate, login
from .models import Recipes


class MyRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'ingredients', 'instructions', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
