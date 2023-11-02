from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Страница приложения women</h1>")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория: {catid}</p>")
