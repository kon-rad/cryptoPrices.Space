from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from coinbase.wallet.client import Client

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@api_view(['GET'])
def prices_list(request):
    # list prices
    client = Client(settings.COINBASE_KEY, settings.COINBASE_SECRET)
    price = client.get_spot_price(currency_pair = 'BTC-USD')
    if request.method == 'GET':
        data = [price]
        return Response({'data': data })
