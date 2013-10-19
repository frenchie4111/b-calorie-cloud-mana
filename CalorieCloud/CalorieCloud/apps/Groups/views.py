from CalorieCloud.helpers import render, redirect
from CalorieCloud.apps.Groups.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

@login_required
def create( request ):
	if( request.method == "GET" ):
		return render( request, "Groups/create.html" )
	elif( request.method == "POST" ):
		if not "name" in request.POST:
			return render( request, "Groups/create.html", { "flash" : "Did not fill in name" } )

		group = Group( name=request.POST["name"], owner=request.user )
		group.save()
		group.users.add( request.user )
		group.save()

		return render( request, "Groups/create.html", { "flash" : "Created Group" } )

@login_required
def group( request, group_id ):
	group = Group.objects.get(pk=group_id)
	if( request.method == "POST" ):
		new_memeber_search = User.objects.filter( email=request.POST["email"] )
		if( len( new_memeber_search ) != 1 ):
			return render( request, "Groups/index.html", {"flash" : "Could Not Find User"} )
		new_member = new_memeber_search[0]
		group.users.add( new_member )
	members = group.users
	return render( request, "Groups/index.html", {"members":members} )

@login_required
def index( request ):
	user = request.user
	groups = user.memberships.all()
	return render( request, "Groups/list.html", {"groups":groups})