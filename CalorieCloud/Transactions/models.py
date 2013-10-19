from django.db import models
from CalorieCloud.apps.UserProfile import UserProfile

# Create your models here.
class Transaction(models.Model):
	"""
	Description: Keeps track of all information from a Transaction
	"""
	name = models.CharField(max_length=254)
	email = models.CharField(max_length=254)
	time = models.DateTimeField()
	amount = models.FloatField()
	recipient = models.ForeignKey(User)	

	def __str__(self):
		return str(self) 
