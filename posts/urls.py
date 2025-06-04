#? Import necesary modules for Accounts app
from django.urls import path
from .views import (
    PostListView,
    PostDraftListView,
    PostArchiveListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='list'),                                 #* List all posts
    path('drafts/', PostDraftListView.as_view(), name='drafts'),                   #* List all draft posts
    path('archive/', PostArchiveListView.as_view(), name='archive'),               #* List all archived posts
    path('create/', PostCreateView.as_view(), name='create'),                      #* Create a new post
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),                 #* Edit an existing post
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),             #* Delete a post
    path('details/<int:pk>/', PostDetailView.as_view(), name='details'),           #* Details a post
]