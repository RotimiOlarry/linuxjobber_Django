from django.shortcuts import render
from django.http import HttpResponse
from timiolarryscrumy.models import *


# Create your views here.
def index(request):
    #return HttpResponse("Welcome to Django")
    response = ScrumyGoals.objects.filter(goal_name ="Learn Django")
    return HttpResponse(response)

def move_goal(request, goal_id):
    resp = ScrumyGoals.objects.get(pk = 1)
    return HttpResponse(resp)


    

