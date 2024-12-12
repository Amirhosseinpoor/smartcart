from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BasketInfoModel

class DateFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class BasketCustomForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BasketInfoModel
        fields = UserCreationForm.Meta.fields + ('basket_id', 'password1', 'password2')


class BasketCustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BasketInfoModel
        fields = UserChangeForm.Meta.fields