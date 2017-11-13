from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from sto.forms import UserForm, StoForm, UserFormEdit, ServiceForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from sto.models import Services, StoService

# Create your views here.
# def index(request):
#     return render(request, 'sto/index.html', {})

def home(request):
    return redirect(sto_home)

@login_required(login_url='/sto/sign-in/')
def sto_home(request):
    return redirect(sto_services)

@login_required(login_url='/sto/sign-in/')
def sto_account(request):
    user_form = UserFormEdit(instance=request.user)
    sto_form = StoForm(instance=request.user.sto)

    if request.method == "POST":
        user_form = UserFormEdit(request.POST, instance=request.user)
        sto_form = StoForm(request.POST, request.FILES, instance=request.user.sto)

        if user_form.is_valid() and sto_form.is_valid():
            user_form.save()
            sto_form.save()

    return render(request, 'sto/account.html', {
        'user_form': user_form,
        'sto_form': sto_form
})

@login_required(login_url='/sto/sign-in/')
def sto_services(request):
    services = StoService.objects.filter(sto=request.user.sto).order_by("-id")
    return render(request, 'sto/services.html', {
        'services': services
})

@login_required(login_url='/sto/sign-in/')
def service_add(request):
    form = ServiceForm()
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.sto = request.user.sto
            service.save()
            return redirect(sto_services)
    return render(request, 'sto/add_service.html', {
        'form': form
})

@login_required(login_url='/sto/sign-in/')
def service_edit(request, service_id):
    form = ServiceForm(instance = StoService.objects.get(id = service_id))
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance = StoService.objects.get(id = sto_id))
        if form.is_valid():
            service = form.save()
            return redirect(sto_services)
    return render(request, 'sto/edit_service.html', {
        'form': form
})

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
