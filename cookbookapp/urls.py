from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
]