from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Group( models.Model ):
	owner = models.ForeignKey( User )
	users = models.ManyToManyField( User, related_name="memberships" )
	name = models.CharField( max_length=254 )
