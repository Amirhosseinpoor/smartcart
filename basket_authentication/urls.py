from django.contrib import admin
from django.urls import path, include
from .views import BasketAuth
urlpatterns = [
    path('basketauthentication/', BasketAuth.as_view(), name='auth'),
]