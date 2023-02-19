from django.shortcuts import render


def index(request):
    cards = {
        1 : {'name': 'Galaxy', 'info': 'Beautiful stars.'},
        2 : {'name': 'Stars', 'info': 'Wonderful world.'}
    }
    return render(request, 'galery/index.html', {'cards': cards})


def image(request):
    return render(request, 'galery/imagem.html')
    