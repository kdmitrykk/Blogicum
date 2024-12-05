from django.http import Http404
from django.shortcuts import render


# posts_dict = {post['id']: post for post in posts}

def index(request):
    """Главная страница проекта."""
    context = {'posts': reversed(posts)}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Страница отдельного блога."""
    try:
        context = {'post': posts_dict[post_id]}
    except KeyError:
        raise Http404(f"Post {post_id} does not exist")
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница отдельной категории."""
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)
