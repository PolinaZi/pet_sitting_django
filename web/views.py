from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout

from web.forms import RegistrationForm, AuthForm, PetForm
from web.models import Pet

User = get_user_model()


def main_view(request):
    return render(request, 'web/main.html')


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {"form": form, "is_success": is_success})


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


def pet_edit_view(request, id=None):
    pet = get_object_or_404(Pet, user=request.user, id=id) if id is not None else None
    form = PetForm(instance=pet)
    if request.method == 'POST':
        form = PetForm(data=request.POST, files=request.FILES, instance=pet, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("pets_add")
    return render(request, "web/pet_form.html", {"form": form})
