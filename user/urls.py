from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name = 'user'),
    path('register', views.register, name = 'register'),
    path('login', views.user_login, name = 'login' ),
    path('logout', views.logout_view, name='logout'),
    path('profile/<slug:username>/', views.getUserProfile)
]