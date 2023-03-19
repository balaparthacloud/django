from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def welcome(request):
    return HttpResponse('welcome to Meeting Planner ! ' + str(datetime.now()))
