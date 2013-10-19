from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserProfileManager( BaseUserManager ):
	"""
	Description: User Profile Management
	"""

	def create_user( self, x_id, first_name, last_name, calories, image, last_updated, calories_paid):
		"""
		Description: creates a client user

		pre:
			x_id (String) - user x_id
			first_name (String) - first name
			last_name (String) - last name
			calories (float) - the amount of calories burned
			image (String) - url of the user's profile image file 
			last_updated (DateTime) = date that the user was last updated
			calories_paid (float) - the amount of calories paid for

		post:
			returns user object
		"""
		user = self.model( x_id=x_id, first_name=first_name, last_name=last_name, calories=calories, image=image, last_updated=laste_updated, calories_paid=calories_paid)
		user.is_admin = False
		user.save()
		return user

	def create_superuser( self, x_id, first_name, last_name, calories, image, last_updated, calories_paid ):
		"""
		Description: creates an admin user
		pre:
			x_id (String) - user x_id
			first_name (String) - first name
			last_name (String) - last name
			calories (float) - the amount of calories burned
			image (String) - url of the user's profile image file 
			last_updated (DateTime) = date that the user was last updated
			calories_paid (float) - the amount of calories paid for

		post:
			returns user object
		"""
		user = self.model( x_id=x_id, first_name=first_name, last_name=last_name, calories=calories, image=image, last_updated=last_updated, calories_paid=calories_paid )
		user.is_admin = True
		user.save()
		return user

class UserProfile( AbstractBaseUser, PermissionsMixin ):
	"""
	Description: User's profile information
	"""
	x_id = models.CharField(max_length=254, unique=True)
	first_name = models.CharField( max_length=254 )
	last_name = models.CharField( max_length=254 )
	image = models.CharField( max_length=254 ) 
	calories = models.FloatField()
	last_updated = models.DateTimeField()
	calories_paid = models.FloatField()

	objects = UserProfileManager()

	is_admin = models.BooleanField( default=False )

	def is_staff( self ):
		return self.is_admin
	def is_active( self ):
		return True
	def has_perm( self, perm, obj=None ):
		return self.is_admin
	def has_module_perms( self, app_label ):
		return self.is_admin
	def get_username( self ):
		return self.email
	def get_short_name( self ):
		return self.first_name + " " + self.last_name