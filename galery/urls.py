from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('image/<int:id>/', views.image, name='image'),
]