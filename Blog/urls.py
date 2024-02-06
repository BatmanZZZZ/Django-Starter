# blogApp/Blog/urls.py
from django.urls import path
from .views import create_post, home, login_view, new_thread, register_view, search_threads, thread_detail

urlpatterns = [
    # Other URL patterns
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),  
    path('new_thread/', new_thread, name='new_thread'),
    path('home/', home, name='home'),
    path('search_thread/', search_threads, name='search_thread'),
    path('thread_detail/<str:thread_id>/',thread_detail , name='thread_detail'),
    path('post_area/<str:thread_id>/',create_post , name='post_area'),
]