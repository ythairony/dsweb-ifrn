from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('enquete/<int:pergunta_id>/', views.detalhes, name='detalhes'),
    path('enquete/<int:pergunta_id>/votacao/', views.votacao, name='votacao'),
    path('enquete/<int:pergunta_id>/resultado/', views.resultado, name='resultado'),
]