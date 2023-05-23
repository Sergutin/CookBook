from django.contrib import admin
from .models import Post, Comment, Recipes
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# @admin.register(Recipes)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     search_fields = ('title', 'description')
#     actions = ['approve_recipes']


#     def approve_recipes(self, request, queryset):
#         queryset.update(approved=True)

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'approved')  # Display the 'approved' field in the admin list
    list_filter = ('approved',)  # Add 'approved' to the admin filter options
    search_fields = ('title',)  # Enable searching by title
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)
    approve_recipes.short_description = "Approve selected recipes"  # Action description

