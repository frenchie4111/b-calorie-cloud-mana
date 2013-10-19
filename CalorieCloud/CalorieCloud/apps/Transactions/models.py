from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Transaction(models.Model):
	"""
	Description: Keeps track of all information from a Transaction

	attributes:
		name (string) - donor's name
		email (string) - donor's email address
		time (DateTime) - time of Transaction
		donation_amount (float) - the amount of money the donor is donating
		calorie_amount (float) - the amount of calories the donor wants the fund
		recipient (FK) - the user getting funded
	"""
	name = models.CharField(max_length=254)
	email = models.CharField(max_length=254)
	time = models.DateTimeField()
	calorie_amount = models.FloatField()
	donation_amount = models.FloatField()
	recipient = models.ForeignKey(User)	

	def __str__(self):
		return str(self) 
