from .models import Comment
from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients', 'instructions')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        