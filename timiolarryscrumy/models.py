from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name =models.CharField(max_length=50, default='')
    user = models.ForeignKey(User, related_name = 'goal_created',on_delete=models.PROTECT)
    goal_name =models.CharField(max_length=50, default='')
    goal_id = models.IntegerField(default=10)
    created_by = models.CharField(max_length=50,default='')
    moved_by =models.CharField(max_length=50,default='')
    owner = models.CharField(max_length=50,default='')
    goal_status = models.ForeignKey(GoalStatus,on_delete=models.PROTECT)

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoals,on_delete=models.PROTECT)
    moved_by = models.CharField(max_length=50,default='')
    created_by = models.CharField(max_length=50,default='')
    moved_from = models.CharField(max_length=50,default='')
    moved_to = models.CharField(max_length=50,default='')
    time_of_action = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.created_by


    

