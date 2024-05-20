from django.shortcuts import render, redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm, CustomUserForm  # Importa el formulario de edición de usuario
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página principal o la que prefieras
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige a la página de login

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def home_view(request):
    return render(request, 'accounts/home.html')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'user/user_detail.html', {'user': user})

def user_edit(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user/user_edit.html', {'form': form})

def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Redirigir a la lista de usuarios después de eliminar
    return render(request, 'user/user_confirm_delete.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirigir a la lista de usuarios después de crear uno nuevo
    else:
        form = CustomUserForm()
    return render(request, 'user/user_create.html', {'form': form})