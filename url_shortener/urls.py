from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createURL/', views.generate_shortURL, name='generate_shortURL'),
    path('<str:url>', views.redirect, name='redirect'), # To accept a url


]

