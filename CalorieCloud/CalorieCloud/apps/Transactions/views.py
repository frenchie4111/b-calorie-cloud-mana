# Create your views here.
from django.http import HttpResponse
from ToolShare.helpers import render, redirect
from CalorieCloud/apps/Transactions import Transaction

def respondToDonation(request, flash = None, flash_negative = False):
	"""
	Description - Render the Donation Page

	pre:
		request - contains all data from the current request
		flash (String) - the string to show in the flash
		flash_negative (boolean) - true for red flash, false for green flash

	post:
		returns a rendered page
	"""
	return render(request, "/Tranactions/donation.html", { "flash" : flash, "flash_negative" : flash_negative})

def donation(request):
	"""
	Description - processes a donation

	pre:
		request - contains all the data from the current request

	post:
		If the request is "GET", show donation page
		If the request is "POST", process the transaction
	"""	
	pass