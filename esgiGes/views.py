from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import Http404


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
