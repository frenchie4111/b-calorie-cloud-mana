from CalorieCloud.apps.UserProfile.models import UserProfile

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
