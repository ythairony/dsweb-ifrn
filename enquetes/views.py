from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Nome: Yuri Thairony Feitosa de Oliveira <br> Matrícula: 20222014040015")