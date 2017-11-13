from django import forms
from django.contrib.auth.models import User
from sto.models import Sto, Services, StoService

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class StoForm(forms.ModelForm):
    class Meta:
        model = Sto
        fields = ('name', 'phone', 'adress', 'logo')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = StoService
        exclude = ('sto',)
