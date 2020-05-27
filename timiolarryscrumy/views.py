from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from timiolarryscrumy.models import ScrumyGoals,GoalStatus
import random


# Create your views here.
def index(request):
    #return HttpResponse("Welcome to Django")
    response = ScrumyGoals.objects.get(goal_name ="Learn Django")
    return HttpResponse(response)

def move_goal(request, goal_id):
    dic = ({"error":"This goal id dooesn't exist"})
    run = {'dict1' : dic }

    try:
        resp = ScrumyGoals.objects.get(goal_id=goal_id)

    except Exception as e:
        return render(request, 'timiolarryscrumy/exception.html' ,run )

    else:
        return HttpResponse(resp.goal_name)
    return HttpResponse(resp)

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
    
    goal = ScrumyGoals.objects.get(goal_name = 'Learn Django')
    dictionary = {
                'goal_name': goal.goal_name, 
                'goal_id': goal.goal_id,
                'user': goal.user
                }
    
    return render(request, 'timiolarryscrumy/home.html', dictionary)