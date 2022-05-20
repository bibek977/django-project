from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    myself = {'name':"bibek"}
    return render(request, 'index.html', myself)

def about(request):
    return HttpResponse("This is a first project")