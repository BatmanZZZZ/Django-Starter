# blogApp/Blog/urls.py
from django.urls import path
from .views import home, login_view, new_thread, register_view, search_threads

urlpatterns = [
    # Other URL patterns
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),  
    path('new_thread/', new_thread, name='new_thread'),
    path('home/', home, name='home'),
    path('search_thread/', search_threads, name='search_thread'),
]