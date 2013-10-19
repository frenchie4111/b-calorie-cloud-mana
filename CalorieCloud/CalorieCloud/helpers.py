from django.shortcuts import render as old_render
from django.http import HttpResponseRedirect

def isNumber( str ):
	"""
		Description:
			Takes a python variable and returns if it is a isNumber

		Pre:
			str - The variable to tell if it is a number or not

		Post:
			Bool - Returns wether or not it is a number
	"""
	try:
		float( str )
		return True
	except ValueError:
		return False

def render( request, page, vars={} ):
	"""
		Description:
			Renders webpage in the main template, passing variables along

		Pre:
			Request - The request to render with
			page - The page to request inside of the default
			vars - Aditional variables to pass along

		Post:
			Returns HTTPResponse with the html template rendered
	"""
	signed_in = request.user.is_authenticated()
	default_values = { "child" : page, "request" : request, "signed_in" : signed_in, "username" : request.user.email if (signed_in) else False }

	varsWithChild = dict(list(default_values.items()) + list(vars.items()))
	return old_render( request, "main.html", varsWithChild )

def redirect( path, vars={} ):
	"""
		Description:
			Returns a redirect response with the given get variables

		Pre:
			path - The path to redirect to
			vars - The variables to pass as get variables

		Post:
			Returns HttpResponseRedirect
	"""
	if( "?" in path ):
		path += "&"
	else:
		path += "?"
	for key in vars:
		path += ( str( key ) + "=" + str( vars[key] ) + "&" )

	return HttpResponseRedirect( path )