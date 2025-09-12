from django.urls import path
from .views import *


urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('book_list/', book_list, name='book_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('toggle_favorite/<int:book_id>/',toggle_favorite, name='toggle_favorite'),
    path('my_favorites/', my_favorites, name='my_favorites'),
    path('add_category/', add_category, name='add_category'),
]
