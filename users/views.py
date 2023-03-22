from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                username=name,
                password=password
            )
            if user is not None:
                messages.success(request, f"{request.POST['name_login']} foi logado com sucesso!")
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, f"Não foi possível logar com {request.POST['name_login']}")
                return redirect('login')


    return render(request, 'users/login.html', {"form": form})


def register(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["password"].value() != form["password2"].value():
                messages.error(request, "Senhas diferentes...")
                return redirect("register")
            
            name = form['name_cadastro'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, f"Já existe um usuário com o nome {name}")
                return redirect('cadastro')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('login')
    
    return render(request, 'users/register.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect("index")