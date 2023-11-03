from django.http import HttpResponse
from django.shortcuts import render

from .models import Women, Category

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()

    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'women/index.html', context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'women/about.html', context)


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория: {catid}</p>")
