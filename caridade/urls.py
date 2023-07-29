from django.urls import path
from . import views

app_name = 'caridade'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('caridade/<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
]
