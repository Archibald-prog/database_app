from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),   # http://127.0.0.1:8000/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about/
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/cats/1/
]
