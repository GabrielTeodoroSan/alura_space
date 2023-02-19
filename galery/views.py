from django.shortcuts import render, get_object_or_404
from .models import Photographs


def index(request):
    photos = Photographs.objects.all()
    return render(request, 'galery/index.html', {'photos': photos})


def image(request, id):
    photo = get_object_or_404(Photographs, pk=id)
    return render(request, 'galery/imagem.html', {'photo': photo})
    