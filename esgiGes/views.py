from django.db import DatabaseError
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from .models import Professor, Student, Image, Cours
from .serializers import ProfessorSerializer, StudentSerializer, getImageSerializer, getCoursSerializer, postImageSerializer, postCoursSerializer
from django.shortcuts import get_object_or_404

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def get_professor(request, id):
    try:
        professor = get_object_or_404(Professor, pk=id)
        serializer = ProfessorSerializer(professor, many=False)
    except DatabaseError:
        return HttpResponse('Professor with id {} not found'.format(id), status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ParseError:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        try:
            Professor.objects.filter(id=id).delete()
            return HttpResponse('Delete successfull', status=status.HTTP_200_OK)
        except DatabaseError:
            return HttpResponse(status=500)
    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            professor.first_name = data['first_name']
            professor.last_name = data['last_name']
            professor.save()
            serializer = ProfessorSerializer(professor, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
        except DatabaseError:
            return HttpResponse('Update failed', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def get_student(request, id):
    try:
        student = get_object_or_404(Student, pk=id)
        serializer = StudentSerializer(student, many=False)
    except DatabaseError:
        return HttpResponse('Professor with id {} not found'.format(id), status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ParseError:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        try:
            Student.objects.filter(id=id).delete()
            return HttpResponse('Delete successfull', status=status.HTTP_200_OK)
        except DatabaseError:
            return HttpResponse(status=500)
    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            student.code = data['code']
            student.name = data['name']
            student.save()
            serializer = ProfessorSerializer(student, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
        except DatabaseError:
            return HttpResponse('Update failed', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def get_image(request, id):
    try:
        image = get_object_or_404(Image, pk=id)
        serializer = StudentSerializer(image, many=False)
    except DatabaseError:
        return HttpResponse('Professor with id {} not found'.format(id), status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ParseError:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        try:
            Image.objects.filter(id=id).delete()
            return HttpResponse('Delete successfull', status=status.HTTP_200_OK)
        except DatabaseError:
            return HttpResponse(status=500)
    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            image.first_name = data['first_name']
            image.last_name = data['last_name']
            image.save()
            serializer = ProfessorSerializer(image, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
        except DatabaseError:
            return HttpResponse('Update failed', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def get_cours(request, id):
    try:
        cours = get_object_or_404(Cours, pk=id)
        serializer = StudentSerializer(cours, many=False)
    except DatabaseError:
        return HttpResponse('Professor with id {} not found'.format(id), status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ParseError:
            return HttpResponse(status=404)

    elif request.method == 'DELETE':
        try:
            Cours.objects.filter(id=id).delete()
            return HttpResponse('Delete successfull', status=status.HTTP_200_OK)
        except DatabaseError:
            return HttpResponse(status=500)
    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            cours.name = data['name']
            cours.save()
            serializer = postCoursSerializer(cours, many=False)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
        except DatabaseError:
            return HttpResponse('Update failed', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        serializer = getImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

        serializer = postImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def getCours(request):
    if request.method == 'GET':
        cours = Cours.objects.all()
        serializer = getCoursSerializer(cours, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=400)

    serializer = postCoursSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
