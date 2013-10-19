from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Event(models.model):
	owner = models.ForeignKey(User)
	description = models.TextField()
	target_calories = models.FloatField()
	target_date = models.DateTimeField()