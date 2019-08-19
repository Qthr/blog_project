from django.urls import path

from .views import BlogListView, BlogDetailVIew

urlpatterns = [
    path('post/<int:pk>/', BlogDetailVIew.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home')
]