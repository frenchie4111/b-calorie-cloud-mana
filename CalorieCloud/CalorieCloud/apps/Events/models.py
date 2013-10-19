from django.db import models
from django.contrib.auth.models import User
from CalorieCloud.apps.Groups.model import Group
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()
# Create your models here.
class Event(models.Model):
	owner = models.ForeignKey(User)
	group_id = models.ForeignKey(Group)
	description = models.TextField()
	target_calories = models.FloatField()
	target_date = models.DateTimeField()
	deadline = models.DateTimeField()