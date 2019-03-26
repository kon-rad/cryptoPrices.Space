from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from coinbase.wallet.client import Client
import os

COIN_EXCHANGES = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD', 'ZRX-USD', 'BCH-USD', 'XLM-USD', 'ETC-USD']

class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
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
