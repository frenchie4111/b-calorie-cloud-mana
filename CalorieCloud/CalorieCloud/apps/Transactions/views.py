# Create your views here.
from django.http import HttpResponse
from CalorieCloud.helpers import render, redirect
from CalorieCloud.apps.Transactions.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

def respondToDonation(resp, request, flash = None, flash_negative = False):
	"""
	Description - Render the Donation Page

	pre:
		request - contains all data from the current request
		flash (String) - the string to show in the flash
		flash_negative (boolean) - true for red flash, false for green flash

	post:
		returns a rendered page
	"""
	return render(request, "Transactions/donation.html", { "resp" : resp, "flash" : flash, "flash_negative" : flash_negative})

def donation(request):
	"""
	Description - processes a donation

	pre:
		request - contains all the data from the current request

	post:
		If the request is "GET", show donation page
		If the request is "POST", process the transaction
	"""	
	if(request.method == "GET"):
		recipient = User.objects.get(pk=request.GET["recipient_id"])
		return respondToDonation(recipient, request, False, False)

	elif(request.method =="POST"):
		try:

			donor = request.user
			time = datetime.datetime.now()
			calorie_amount = request.POST["calorie_amount"]
			donation_amount = request.POST["donation_amount"]
			

		except(KeyError):
			return respondToDonation(request, "Something went terribly wrong", True)

		else:
			transaction = Transaction(first_name=first_name, last_name=last_name, email=email, time=time, calorie_amount=calorie_amount, donation_amount=donation_amount, recipient=recipient)
			transaction.save()
			return redirect("/transaction", {"Transaction Successful" : "True"})