from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@api_view(['GET'])
def prices_list(request):
    # list prices
    if request.method == 'GET':
        data = ['helloworld']
        return Response({'data': data })
