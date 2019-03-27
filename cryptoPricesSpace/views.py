from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from coinbase.wallet.client import Client
import os

COIN_EXCHANGES = [
    'BTC-USD',
    'ETH-USD',
    'XRP-USD',
    'LTC-USD',
    'BCH-USD',
    'XLM-USD',
    'ETC-USD',
    'ZEC-USD',
    'BAT-USD',
    'USDC-USD',
    'ZRX-USD'
    ]

class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                This page is currently unavailable. Please try again later.
                """,
                status=501,
            )

@api_view(['GET'])
def prices_list(request):
    client = Client(settings.COINBASE_KEY, settings.COINBASE_SECRET)
    price = []
    for coin in COIN_EXCHANGES:
        price.append(client.get_spot_price(currency_pair = coin))
    if request.method == 'GET':
        return Response({'data': price})
