from CalorieCloud.helpers import render, redirect
from CalorieCloud.apps.Groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

def create( request ):
	if( request.method == "GET" ):
		return render( request, "Groups/create.html" )
	elif( request.method == "POST" ):
		if not "name" in request.POST:
			return render( request, "Groups/create.html", { "flash" : "Did not fill in name" } )

		Group( name=request.POST["name"], owner=request.user ).save()

		return render( request, "Groups/create.html", { "flash" : "Created Group" } )

def group( request, group_id ):
	if( request.method == "POST" ):
		new_memeber_search = User.objects.filter( email=request.POST["email"] )
		if( len( new_memeber_search ) != 1 ):
			return render( request, "Groups/index.html", {"flash" : "Could Not Find User"} )
		new_member = new_memeber_search[0]
		Group.users.add( new_member )
	members = Group.objects.get(pk=group_id).users
	return render( request, "Groups/index.html", {"members":members} )