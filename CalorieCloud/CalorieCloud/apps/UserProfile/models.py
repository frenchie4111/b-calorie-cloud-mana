from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class UserProfileManager( BaseUserManager ):
	"""
	Description: User Profile Management
	"""

	def create_user( self, email, x_id="", first_name="", last_name="", calories=0, image="", last_updated=datetime.datetime.now(), calories_paid=0, password=None):
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
		user.set_password("blank")
		return user

	def create_superuser( self, email, x_id="", first_name="", last_name="", calories=0, image="", last_updated=datetime.datetime.now(), calories_paid=0, password=None ):
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
		user.set_password(password)
		user.save()
		return user

class UserProfile( AbstractBaseUser, PermissionsMixin ):
	"""
	Description: User's profile information
	"""
	email = models.CharField(max_length=254, unique=True)
	x_id = models.CharField(max_length=254)
	first_name = models.CharField( max_length=254 )
	last_name = models.CharField( max_length=254 )
	image = models.CharField( max_length=254 ) 
	calories = models.FloatField()
	last_updated = models.DateTimeField()
	calories_paid = models.FloatField()

	objects = UserProfileManager()

	is_admin = models.BooleanField( default=False )

	USERNAME_FIELD = 'email'

	def is_staff( self ):
		return self.is_admin
	def is_active( self ):
		return True
	def has_perm( self, perm, obj=None ):
		return self.is_admin
	def has_module_perms( self, app_label ):
		return self.is_admin
	def get_username( self ):
		return self.x_id
	def get_short_name( self ):
		return self.first_name + " " + self.last_name