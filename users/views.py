from django.shortcuts import render
from .forms import LoginForms, CadastroForms

# Create your views here.

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {"form": form})


def register(request):
    form = CadastroForms()
    return render(request, 'users/register.html', {"form": form})


def logout(request):
    return render(request, 'users/logout.html')