from django.contrib.auth.views import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class BasketAddress(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'