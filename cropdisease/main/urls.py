# main/urls.py
from django.urls import path
from .views import register, communication_page, edit_query, delete_query, home

urlpatterns = [
    path('communication/', communication_page, name='communication_page'),
    path('edit_query/<int:query_id>/', edit_query, name='edit_query'),
    path('delete_query/<int:query_id>/', delete_query, name='delete_query'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
]
