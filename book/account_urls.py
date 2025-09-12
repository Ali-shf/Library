from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.login_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]