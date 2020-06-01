from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from timiolarryscrumy.models import ScrumyGoals,GoalStatus
import random


# Create your views here.
def index(request):
    response = ScrumyGoals.objects.get(goal_name ="Learn Django")
    return HttpResponse(response)

def move_goal(request, goal_id):
    try:
        resp = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
        return render(request, 'timiolarryscrumy/exception.html' ,{'error':'A record with that goal id does not exist'})
    else:
        return HttpResponse(resp.goal_name)

def add_goal(request):
    goal_dict = {}
    number = random.randint(1000, 9999)
    if number not in goal_dict:
        add = ScrumyGoals.objects.create(
            goal_name = "Keep Learning Django", 
            goal_id = number,
            created_by = 'Louis',
            moved_by = 'Louis',
            owner = 'Louis',
            user = User.objects.get(username ='LouisOma'),
            goal_status = GoalStatus.objects.get(status_name = 'Weekly Goal'))
        goal_dict[number] = number
    return HttpResponse(add)

def home(request):
    user = User.objects.all()

    dictionary = {
                'user': user
                }
    
    return render(request, 'timiolarryscrumy/home.html', dictionary)