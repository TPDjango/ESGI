
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from .models import Professor, Student, Image, Cours
from .serializers import ProfessorSerializer, StudentSerializer, getImageSerializer, getCoursSerializer, postImageSerializer , postCoursSerializer


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def get_professor(request, id):
    if request.method == 'GET':
        # professor = get_object_or_404(Professor, pk=prof_id)
        return HttpResponse("Prof is is {0}".format(id))
    elif request.method == 'DELETE':
        return HttpResponse("Prof is is {0}".format(id))


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
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

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
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

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
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

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
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
