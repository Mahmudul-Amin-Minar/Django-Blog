from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'publish']
    list_filter = ['author', 'created']
    search_fields = ['title', 'body', 'author', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    raw_id_fields = ('author',)

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

admin.site.register(Comment, CommentAdmin)



