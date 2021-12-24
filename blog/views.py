from django.shortcuts import render
from django.http import HttpResponse
def Home(request):
    return HttpResponse("<H1>Hello World</H1>")
# Create your views here.
