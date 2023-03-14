from django.shortcuts import render, get_object_or_404
from .models import Photographs


def index(request):
    photos = Photographs.objects.order_by("-date_photo").filter(published=True)
    return render(request, 'galery/index.html', {'photos': photos})


def image(request, id):
    photo = get_object_or_404(Photographs, pk=id)
    return render(request, 'galery/imagem.html', {'photo': photo})


def search(request):
    photos = Photographs.objects.order_by("-date_photo").filter(published=True)

    if "search" in request.GET:
        s_name = request.GET["search"]
        if s_name:
            photos = photos.filter(name__icontains=s_name)
            
    return render(request, 'galery/search.html', {"photos": photos})