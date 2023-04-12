from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .scraper import getRestaurants

# Create your views here.
@api_view(['GET'])
def getData(request):
    res = getRestaurants(request.GET['city'], request.GET['food'])
    return Response(res)
