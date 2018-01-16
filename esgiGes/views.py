from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import Http404
from .models import Professor
from .serializers import ProfessorSerializer

from .models import Professor


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getProfessors(request):
    if request.method == 'GET':
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

    serializer = ProfessorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)