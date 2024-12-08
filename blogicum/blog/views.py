import datetime

from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post

post_list = Post.objects.select_related('category',
                                        'author',
                                        'location').filter(
                                            is_published=True,
                                            category__is_published=True,
                                            pub_date__lte=datetime.
                                            datetime.now(
                                            ))

category = Category.objects.values('title',
                                   'description').filter(is_published=True)


def index(request):
    """Главная страница проекта."""
    post_list_limit = post_list[0:5]
    context = {'post_list': post_list_limit}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Страница отдельного блога."""
    post = get_object_or_404(post_list.filter(pk=post_id))
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница отдельной категории."""
    this_category = get_object_or_404(category, slug=category_slug)
    post_list_category = post_list.filter(category__slug=category_slug)
    context = {'post_list': post_list_category,
               'category': this_category}
    return render(request, 'blog/category.html', context)
