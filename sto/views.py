from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from sto.forms import UserForm, StoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'sto/index.html', {})

def home(request):
    return redirect(sto_home)

@login_required(login_url='/sto/sign-in/')
def sto_home(request):
    return render(request, 'sto/home.html', {})

@login_required(login_url='/sto/sign-in/')
def sto_account(request):
    return render(request, 'sto/account.html', {})

@login_required(login_url='/sto/sign-in/')
def sto_services(request):
    return render(request, 'sto/services.html', {})

def sto_sign_up(request):
    user_form = UserForm()
    sto_form = StoForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        sto_form = StoForm(request.POST, request.FILES)

        if user_form.is_valid() and sto_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_sto = sto_form.save(commit=False)
            new_sto.owner = new_user
            new_sto.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))
            return redirect(sto_home)

    return render(request, 'sto/sign_up.html', {
        'user_form': user_form,
        'sto_form': sto_form
})
