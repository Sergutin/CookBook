from .models import Comment, Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']  # Add the 'description' field to the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        