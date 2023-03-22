from django.shortcuts import render, get_object_or_404, redirect
from .models import Photographs
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para acessar a página de fotos.")
        return redirect('login')
    
    photos = Photographs.objects.order_by("-date_photo").filter(published=True)
    return render(request, 'galery/index.html', {'photos': photos})


def image(request, id):
    photo = get_object_or_404(Photographs, pk=id)
    return render(request, 'galery/imagem.html', {'photo': photo})


def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado...")
        print("hello................")
        return redirect('login')
    
    photos = Photographs.objects.order_by("-date_photo").filter(published=True)

    if "search" in request.GET:
        s_name = request.GET["search"]
        if s_name:
            photos = photos.filter(name__icontains=s_name)
            
    return render(request, 'galery/search.html', {"photos": photos})