from django.urls import path
from .views import ForumListAPIView, ForumDetailAPIView, TopicListAPIView, TopicDetailAPIView, CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    path('forums/', ForumListAPIView.as_view(), name='forum-list'),
    path('forums/<int:pk>/', ForumDetailAPIView.as_view(), name='forum-detail'),
    path('topics/', TopicListAPIView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetailAPIView.as_view(), name='topic-detail'),
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]
