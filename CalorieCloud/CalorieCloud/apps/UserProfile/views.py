from CalorieCloud.apps.UserProfile.models import UserProfile
from CalorieCloud.helpers import render, redirect
import urllib2, json
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
	if( not user ):
		return redirect( "/" )

	return render( request, "UserProfile/profile.html" )

def login( request ):
	# Check if expired!
	req = urllib2.Request( "https://jawbone.com/auth/oauth2/token/?client_id=6-jb89a0fSQ&client_secret=30f5af7938b1e51ee6e498c07641b33743e972ba&grant_type=authorization_code&code=" + request.GET["code"] )
	res = urllib2.urlopen( req )

	res_dict = json.loads(res.read())

	info_req = urllib2.Request( "https://jawbone.com/nudge/api/v.1.0/users/@me" )
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	info_req.add_header( "Accept", "pplication/json")
	info_req.add_header( "Authorization", "Bearer " + res_dict["access_token"] )
	info_res = urllib2.urlopen( info_req )

	user = 

	return render( request, "UserProfile/login.html", { "flash" : info_res.read() } )