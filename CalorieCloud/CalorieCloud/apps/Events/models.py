from django.db import models
from django.contrib.auth.models import User
from CalorieCloud.apps.Groups.models import Group
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()
# Create your models here.
class Event(models.Model):
	owner = models.ForeignKey(User)
	group = models.ForeignKey(Group)
	description = models.TextField()
	target_calories = models.FloatField()
	target_date = models.CharField(max_length=264)
	deadline = models.CharField(max_length=264)

	def __str__(self):
		return self.owner.first_name + " " + self.owner.last_name