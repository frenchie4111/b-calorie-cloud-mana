from CalorieCloud.apps.UserProfile.models import UserProfile
from CalorieCloud.helpers import render, redirect
import urllib2, json
from django.contrib.auth import get_user_model
import datetime

from django.contrib.auth import authenticate as auth, login as auth_login, logout as auth_logout

User = get_user_model()

def profile_page( request, user_id=None ):
	"""
		Description:
			Renders profile_page for a user, if no user id is given then renders the logged in user

		Pre:
			Request - the request
			user_id - The is of the user

		Post:
			Returns HTTPResponse with user profile page
	"""
	user = None
	if( user_id ):
		user = UserProfile.get(pk=user_id)
	else:
		user = request.user

	return render( request, "UserProfile/profile.html", { "user" : user } )

def register( request ):
	if( request.method == "GET" ):
		return render( request, "UserProfile/register.html" )
	elif( request.method == "POST" ):
		new_user = User( email=request.POST["username"] )
		new_user.first_name = request.POST["first_name"]
		new_user.last_name = request.POST["last_name"]
		new_user.calories = 0
		new_user.calories_paid = 0
		new_user.last_updated = datetime.datetime.now()
		if( request.POST["password"] != request.POST["password2"] ):
			return render( request, "UserProfile/register.html", { "flash" : "Passwords did not match", "flash_negative" : True } )
		new_user.set_password( request.POST["password"] )
		new_user.save()

		auth_user = auth( email=request.POST["username"], password=request.POST["password"] )
		auth_login( request, auth_user )

		return redirect( "/user/link_jawbone" )

def login( request ):
	if( request.method == "GET" ):
		return render( request, "UserProfile/login.html" )
	elif( request.method == "POST" ):
		user = auth( email=request.POST["username"], password=request.POST["password"] )
		auth_login( request, user )
		return redirect( "/?login_success" )

def logout( request ):
	auth_logout( request )
	return redirect( "/" )

def link_jawbone( request ):
	if( request.method == "GET" ):
		if( request.user.x_id ):
			return redirect( "/" )
		if( "code" in request.GET ): # Response from Jawbone
			token, info = get_user_info( request.GET["code"] )
			user = request.user
			user.x_id = info["meta"]["user_xid"]
			user.image = info["data"]["image"]
			user.access_token = token
			user.save()
			return redirect( "/" )
		else: #Otherwise do this
			return render( request, "UserProfile/link_jawbone.html")
	elif( request.method == "POST" ):
		pass

def update_calories( request ):
	req = urllib2.Request( "https://jawbone.com/nudge/api/v.1.0/users/@me/trends?range_duration=500&range=w&bucket_size=y" )
	req.add_header( "Authorization", "Bearer " + request.user.access_token )
	res = urllib2.urlopen( req )
	res_dict = json.loads(res.read())
	user = request.user
	user.calories = res_dict["data"]["data"][0][1]["m_calories"]
	user.save()
	return render( request, "core/home_page.html", { "flash" : str(res_dict["data"]["data"][0][1]["m_calories"]) } )

def get_calorie_count( request ):
	pass

def get_user_info( code ):
	req = urllib2.Request( "https://jawbone.com/auth/oauth2/token/?client_id=6-jb89a0fSQ&client_secret=30f5af7938b1e51ee6e498c07641b33743e972ba&grant_type=authorization_code&code=" + code )
	res = urllib2.urlopen( req )

	res_dict = json.loads(res.read())

	info_req = urllib2.Request( "https://jawbone.com/nudge/api/v.1.0/users/@me" )
	info_req.add_header("Content-type", "application/x-www-form-urlencoded")
	info_req.add_header( "Accept", "application/json")
	info_req.add_header( "Authorization", "Bearer " + res_dict["access_token"] )
	info_res = urllib2.urlopen( info_req )
	info_dict = json.loads(info_res.read())

	return res_dict["access_token"], info_dict