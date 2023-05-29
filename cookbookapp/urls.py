from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
    path(
        'delete_recipe/<int:recipe_id>/',
        views.delete_recipe,
        name='delete_recipe'
        ),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
