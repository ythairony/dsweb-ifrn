from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('encerradas/', views.EncerradasView.as_view(), name='encerradas'),
    path('enquete/<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    path('enquete/<int:pk>/votacao/', views.VotacaoView.as_view(), name='votacao'),
    path('enquete/<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),
]