from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ToDoApp(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.CharField('Add Task',max_length=1000)
    datetime = models.DateTimeField(default=timezone.now)
