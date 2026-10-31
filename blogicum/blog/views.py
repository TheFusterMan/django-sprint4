from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_LIMIT = 5


def get_published_posts():
    """Возвращает queryset опубликованных постов с тремя условиями."""
    return Post.objects.select_related(
        'category',
        'location',
        'author',
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    """Главная страница: 5 последних опубликованных постов."""
    post_list = get_published_posts()[:POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    post = get_object_or_404(get_published_posts(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница постов выбранной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.posts.select_related(
        'location',
        'author',
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
