from django.shortcuts import render
from django.views.generic import TemplateView

class BlogBasket(TemplateView):
    template_name = 'index.html'
# Create your views here.
