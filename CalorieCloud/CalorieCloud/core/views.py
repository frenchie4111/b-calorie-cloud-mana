from django.http import HttpResponse
from CalorieCloud.helpers import render, redirect

def respondToHomePage( request, flash, flash_negative ):
	logged = request.user.is_authenticated()
	return render( request, "core/home_page.html", { "flash" : flash, "flash_negative" : flash_negative } )

def home_page( request ): # Render Homepage
	# if(not request.user.is_authenticated()):
	# 	return redirect("/register")
	# if( "logged" in request.GET and request.user.is_authenticated() ):
	# 	return respondToHomePage( request, "Logged In", False )
	# if( "already_logged" in request.GET and request.user.is_authenticated() ):
	# 	return respondToHomePage( request, "Already Logged In", True )
	# if( "registered" in request.GET ):
	# 	return respondToHomePage( request, "Account creation successful", False )
	# if( "shed_created" in request.GET ):
	# 	return respondToHomePage( request, "Shed creation successful", False )
	return respondToHomePage( request, False, False )