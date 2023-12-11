from django.contrib import admin
from .models import Forum, Comment, Reply, Tag, Visit, ForumVote, CommentVote

# Register your models here.
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)    
admin.site.register(Visit)
admin.site.register(ForumVote)
admin.site.register(CommentVote)
