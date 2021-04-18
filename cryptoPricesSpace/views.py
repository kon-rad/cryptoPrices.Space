from django.http import HttpResponse
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from pycoingecko import CoinGeckoAPI
import os


cg = CoinGeckoAPI()

COINS_IDS = [
    'bitcoin', 
    'ethereum',
    'ripple',
    'binancecoin',
    'tether',
    'cardano',
    'polkadot',
    'dogecoin',
    'litecoin', 
    'bitcoin-cash', 
    'stellar',
    'wrapped-bitcoin',
    'iota',
    'monero',
    'decentraland'
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

    price = cg.get_price(ids=COINS_IDS, vs_currencies='usd')
    sortedPrice = []

    for item in COINS_IDS:
        coinData = cg.get_coin_by_id(item)
        priceData = {};
        priceData['base'] = coinData['name']
        priceData['currency'] = 'USD'
        priceData['amount'] = price[item]['usd']
        sortedPrice.append(priceData)
    if request.method == 'GET':
        return Response({'data': sortedPrice})
