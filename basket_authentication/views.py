from django.contrib.auth.views import reverse_lazy
from django.views.generic import CreateView
from .forms import BasketCustomForm

class BasketAuth(CreateView):
    form_class = BasketCustomForm
    template_name = 'registration/auth.html'