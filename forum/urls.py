from django.urls import path
from .views import (
    ForumListView,
    ForumDetailView,
    ForumCreateView,
    ForumUpdateView,
    ForumDetailView,
    ForumDeleteView,
    CommentCreateView
)
from . import views

urlpatterns = [
    path('forum/', ForumListView.as_view(), name='forum'),
    path('forum/<int:pk>/', ForumDetailView.as_view(), name='forum-detail'),
    path('forum/new/', ForumCreateView.as_view(), name='forum-create'),
    path('forum/<int:pk>/update/', ForumUpdateView.as_view(), name='forum-update'),
    path('forum/<int:pk>/delete/', ForumDeleteView.as_view(), name='forum-delete'),
    path('forum/<int:pk>/comment/',
         CommentCreateView.as_view(), name='forum-comment'),

]
