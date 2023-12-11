from django.urls import path
from forums import views

urlpatterns = [
    path('forum', views.ForumView.as_view(), name='forum'),
    path('forum/<int:forum_id>', views.ForumDetailView.as_view(), name='forum-detail'),
    path('forum/vote-forum/<int:forum_id>', views.VoteForum.as_view(), name='vote-forum'),
    path('forum/vote-comment/<int:comment_id>', views.VoteComment.as_view(), name='vote-comment'),
    path('forum/post-comment/<int:forum_id>', views.PostComment.as_view(), name='post-comment'),
    path('forum/post-reply/<int:comment_id>', views.PostReply.as_view(), name='post-reply'),

]