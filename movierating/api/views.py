from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse("hello")

def hello():
    return HttpResponse("hai")