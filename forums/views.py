from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Forum, Visit, Comment, Reply, Tag, ForumVote, CommentVote
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class ForumView(View):
    def get(self, request):
        forums = Forum.objects.all()
        for forum in forums:
            forum.tags = Tag.objects.filter(forum=forum)
            forum.view_count = Visit.objects.filter(forum=forum).count()
            forum.comment_count = Comment.objects.filter(forum=forum).count()
            forum.votes = ForumVote.objects.filter(forum=forum, vote='like').count() - ForumVote.objects.filter(forum=forum, vote='dislike').count()
        hot_forums = sorted(forums, key=lambda forum: forum.view_count, reverse=True)[:5]
        return render(request, 'forum.html', {
            'forums': forums.order_by('-date_created'),
            'hot_forums': hot_forums,
        })

    def post(self, request):
        user = request.user
        title = request.POST['forum-title']
        description = request.POST['forum-content']
        forum = Forum.objects.create(user=user, title=title, description=description)
        forum.save()
        tags = request.POST['forum-tags']
        tags = [tag.replace('#','') for tag in tags.split(' ')]
        for tag in tags:
            Tag.objects.create(forum=forum, tag=tag).save()

        return render(request, 'my-forum.html')    

class ForumDetailView(View):
    def get(self, request, forum_id):
        forum = Forum.objects.get(id=forum_id)
        is_visited = Visit.objects.filter(user=request.user, forum=forum_id)
        if not is_visited:
            Visit.objects.create(user=request.user, forum=forum).save()                
        forum.tags = Tag.objects.filter(forum=forum)
        forum.comments = Comment.objects.filter(forum=forum)
        for comment in forum.comments:
            comment.replies = Reply.objects.filter(comment=comment)
            comment.votes = CommentVote.objects.filter(comment=comment, vote='like').count() - CommentVote.objects.filter(comment=comment, vote='dislike').count()
        forum.view_count = Visit.objects.filter(forum=forum).count()
        forum.comment_count = Comment.objects.filter(forum=forum).count()
        forum.votes = ForumVote.objects.filter(forum=forum, vote='like').count() - ForumVote.objects.filter(forum=forum, vote='dislike').count()
        hot_forums = sorted(Forum.objects.all(), key=lambda forum: Visit.objects.filter(forum=forum).count(), reverse=True)[:5]
        return render(request, 'detail-forum.html', {
            'forum': forum,
            'hot_forums': hot_forums,
        })

class PostComment(View):
    def post(self, request, forum_id):
        user = request.user
        forum = Forum.objects.get(id=forum_id)
        comment = request.POST['content']
        Comment.objects.create(user=user, forum=forum, comment=comment).save()            
        
        return redirect('forums:forum-detail', forum_id=forum_id)

class PostReply(View):
    def post(self, request, comment_id):
        user = request.user
        comment = Comment.objects.get(id=comment_id)
        reply = request.POST['content']
        Reply.objects.create(user=user, comment=comment, reply=reply).save()
        return redirect('forums:forum-detail', forum_id=comment.forum.id)

class VoteForum(View):
    def post(self, request, forum_id):
        user = request.user
        forum = Forum.objects.get(id=forum_id)
        vote = request.POST['vote']
        user_vote = ForumVote.objects.filter(user=user, forum=forum)
        if user_vote:
            user_vote = user_vote[0]
            if user_vote.vote == vote:
                user_vote.delete()
            else:
                user_vote.vote = vote
                user_vote.save()
        else:
            ForumVote.objects.create(user=user, forum=forum, vote=vote).save()
        
        return redirect('forums:forum-detail', forum_id=forum_id)

class VoteComment(View):
    def post(self, request, comment_id):
        user = request.user
        comment = Comment.objects.get(id=comment_id)
        vote = request.POST['vote']
        user_vote = CommentVote.objects.filter(user=user, comment=comment)
        if user_vote:
            user_vote = user_vote[0]
            if user_vote.vote == vote:
                user_vote.delete()
            else:
                user_vote.vote = vote
                user_vote.save()
        else:
            CommentVote.objects.create(user=user, comment=comment, vote=vote).save()

        return redirect('forums:forum-detail', forum_id=comment.forum.id)