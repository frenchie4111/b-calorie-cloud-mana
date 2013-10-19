# Create your views here.
from django.http import HttpResponse
from CalorieCloud.helpers import render, redirect
from django.contrib.auth.models import User
from CalorieCloud.apps.Groups.models import Group
from CalorieCloud.apps.Events.models import Event
from django.contrib.auth import get_user_model
import datetime, urllib as urllib2, json
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def eventList(request, flash=False, flash_negative=False):
	group_list = request.user.memberships.all()
	events_list = []
	for group in group_list:
		events_list.extend(group.event_set.all())
	return render(request, "Events/event_list.html", {"events_list" : events_list})

@login_required
def index(request, event_id, flash=False, flash_negative = False):
	event = Event.objects.get(pk=event_id)
	return render(request, "Events/index.html",{ "flash" : flash, "flash_negative" : flash_negative, "event" : event})

@login_required
def respondToEventCreation(request, flash=False, flash_negative=False):
	groups = Group.objects.filter(owner = request.user)
	return render(request, "Events/event_creation.html", { "flash" : flash, "flash_negative" : flash_negative, "groups" : groups })

@login_required
def eventCreation(request, flash=False, flash_negative=False):
	if (request.method == "GET"):
		return respondToEventCreation(request)
	elif (request.method == "POST"):
		try:
			owner = request.user
			description = request.POST["description"]
			target_calories = request.POST["target_calories"]
			target_date = request.POST["target_date"]
			group = Group.objects.get(pk=request.POST["group"])
			deadline = request.POST["deadline"]
			
		except(KeyError):
			return respondToEventCreation(request,str(KeyError), True)

		else:
			event = Event.objects.create(owner=owner, group=group, description=description, target_calories=target_calories, target_date=target_date, deadline=deadline)
			return render(request, "Events/index.html", { "flash" : flash, "flash_negative" : flash_negative, "event" : event})