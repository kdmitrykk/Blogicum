from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post


POSTS_PER_PAGE = 5


def index(request):
    """Главная страница проекта."""
    post_list = Post.published.all()
    post_list = post_list[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Страница отдельного блога."""
    post = get_object_or_404(Post.published, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница отдельной категории."""
    category = get_object_or_404(Category.objects.values('title',
                                                         'description'),
                                 slug=category_slug,
                                 is_published=True)
    post_list = Post.published.filter(category__slug=category_slug)
    context = {'post_list': post_list,
               'category': category}
    return render(request, 'blog/category.html', context)
