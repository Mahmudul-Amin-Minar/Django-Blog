from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm, PostCreateForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


def my_posts(request):
    posts = Post.published.filter(author=request.user)
    total = posts.count()
    return render(request, 'blog/post/my_posts.html', {'posts': posts, 'total': total})


def post_detail(request, id):
    post = get_object_or_404(Post, status='published', id=id)

    # comment system
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.email = request.user.email
            new_comment.save()
            return redirect('blog:post_detail', post.id)
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form,
                                                     'similar_posts': similar_posts})


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog:home')
    else:
        form = PostCreateForm()
    return render(request, 'blog/post/create_post.html', {'form': form})


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.user == post.author:
        post.delete()
        return redirect('blog:home')
    else:
        return render(request, 'blog/warning.html')


@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostCreateForm(request.POST, instance=post)
            form.save()
            return redirect('blog:home')

        else:
            form = PostCreateForm(instance=post)
            return render(request, 'blog/post/create_post.html', {'form': form})
    else:
        return render(request, 'blog/warning.html')
