# Create your views here.
from django.http import HttpResponse
from CalorieCloud.helpers import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime, urllib as urllib2, json

User = get_user_model()

def respondToIndex(request, flash=False, flash_negative=False):
	return render(request, "Events/index.html",{ "flash" : flash, "flash_negative" : flash_negative})


def respondToEventCreation(request, flash=False, flash_negative=False):
	return render(request, "Events/event_creation.html", { "flash" : flash, "flash_negative" : flash_negative})

def eventCreation(request, flash=False, flash_negative=False):
	if (request.method == "GET"):
		return respondToEventCreation(request)
	elif (request.method == "POST"):
		try:
			owner = request.user
			description = request.POST["description"]
			target_calories = request.POST["target_calories"]
			target_date = request.POST["target_date"]
			deadline = request.POST["deadline"]
		except(KeyError):
			return respondToEventCreation(request,KeyError, True)

		else:
			event = Event(owner, description, target_calories, target_date, deadline)
			event.save()
			return render(request,"Events/index.html",{ "flash" : flash, "flash_negative" : flash_negative, "event_name" : event.name})