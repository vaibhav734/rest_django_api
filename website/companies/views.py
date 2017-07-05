from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
import json
# Create your views here.

# List all stocks or create a new one
# stocks/FB/
# class StockList(APIView):
#
#     def get(self, request, ticker=None):
#         stocks = Stock.objects.all()
#         if ticker:
#             stocks = Stock.objects.get(ticker=ticker)
#             # stocks = get_object_or_404(Stock, ticker=ticker)
#         serializer = StockSerializer(stocks, many=True)
#         return Response(serializer.data)
#         # return HttpResponse(json.dumps({'stocks':stocks.to_dict()}))
#
#     def post(self):
#         pass

@api_view(['GET', 'POST'])
def stock_list(request, ticker=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        stocks = Stock.objects.all()
        if ticker:
            stocks = stocks.filter(ticker=ticker)
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)