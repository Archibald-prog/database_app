from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    # cats = Category.objects.all()

    context = {
        'menu': menu,
        'title': 'Главная страница',
        # 'cats': cats,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'women/about.html', context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': posts[0].cat_id,
    }
    return render(request, 'women/index.html', context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context)
