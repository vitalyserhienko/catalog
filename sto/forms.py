from django import forms
from django.contrib.auth.models import User
from sto.models import Sto

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class StoForm(forms.ModelForm):
    class Meta:
        model = Sto
        fields = ('name', 'phone', 'adress', 'logo')
