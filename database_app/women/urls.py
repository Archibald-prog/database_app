from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about/
    path('addpage/', addpage, name='add_page'),  # http://127.0.0.1:8000/addpage/
    path('contact/', contact, name='contact'),   # http://127.0.0.1:8000/contact/
    path('login/', login, name='login'),  # http://127.0.0.1:8000/login/
    path('post/<slug:post_slug>/', show_post, name='post'),   # http://127.0.0.1:8000/post/madonna/
    path('cats/<slug:cat_slug>/', show_category, name='category'),   # http://127.0.0.1:8000/cats/aktrisyi/
]
