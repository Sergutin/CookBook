from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Recipes
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from .forms import MyRecipeForm

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = MyRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            print(recipe)
            recipe.author = request.user
            recipe.save()
            # return redirect('recipe_detail', recipe_id=recipe.id)
        else:
            print("Error")
    else:
        form = MyRecipeForm()
    return render(request, 'create_recipe.html', {'form': form})


@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if recipe.author != request.user:
        return redirect('post_detail', slug=recipe.slug)

    if request.method == 'POST':
        form = MyRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=recipe.slug)
    else:
        form = MyRecipeForm(instance=recipe)
    return render(request, 'update_recipe.html', {'form': form, 'recipe': recipe})



@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    if request.method == 'POST' and request.user == recipe.author:
        recipe.delete()
        return redirect('home')
    else:
        # Handle unauthorized access or other cases
        return redirect('home')

    
# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 6

class PostList(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_recipes'] = Recipes.objects.filter(approved=True)
        return context




class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        