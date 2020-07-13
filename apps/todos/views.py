from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def todos(request):
    return HttpResponse("Hello from todos page")