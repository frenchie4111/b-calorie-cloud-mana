from django.conf.urls import patterns, url

from CalorieCloud.apps.Groups import views
urlpatterns = patterns('',
	url(r'^create', views.create, name='create'),
	url(r'^(\d?)/$', views.group, name='group'),
	url(r'^$', views.index, name='index'),
)