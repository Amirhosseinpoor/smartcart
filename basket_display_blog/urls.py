from django.contrib import admin
from django.urls import path, include
from .views import BlogBasket
urlpatterns = [
    path('blog/', BlogBasket.as_view(), name='blog'),

]