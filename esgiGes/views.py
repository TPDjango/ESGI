from django.db import DatabaseError
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from .models import Professor, Student, Image, Cours
from .serializers import ProfessorSerializer, StudentSerializer, ImageSerializer, CoursSerializer
from django.shortcuts import get_object_or_404
from .serializers import ProfessorSerializer, StudentSerializer, getImageSerializer, getCoursSerializer, postImageSerializer , postCoursSerializer


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def get_professor(request,id):
    if request.method == 'GET':
        try:
            professor = get_object_or_404(Professor, pk=id)
            serializer = ProfessorSerializer(professor, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ParseError:
            return HttpResponse(status=404)
    elif request.method == 'DELETE':
        try:
            Professor.objects.filter(id=id).delete()
            return HttpResponse('Delete successfull', status=status.HTTP_200_OK)
        except DatabaseError:
            return HttpResponse(status=500)


@csrf_exempt
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


@csrf_exempt
def getStudents(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def getImages(request):
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

        #print(data.get('student'))
        serializer = StudentSerializer(data=data.get('student'))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def getCours(request):
    if request.method == 'GET':
        cours = Cours.objects.all()
        serializer = CoursSerializer(cours, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

    serializer = CoursSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
