from django.contrib import admin

from .models import Post, PostFile, Comment, Like


class PostFileInlineAdmin(admin.TabularInline):
    model = PostFile
    fields = ('file',)
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'user', 'is_approved')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_active', 'created_time')
    inlines = (PostFileInlineAdmin,)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('is_like', 'post', 'user')

