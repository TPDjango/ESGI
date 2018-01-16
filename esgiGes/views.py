from django.shortcuts import render
from django.http import HttpResponse

from .models import Professor

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def professors(request):
    professors_list = Professor.objects.all()
    output = ', '.join([p.first_name for p in professors_list])
    return HttpResponse(output)