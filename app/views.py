from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def kanna(request):
    return  HttpResponse("kanna is good boy")