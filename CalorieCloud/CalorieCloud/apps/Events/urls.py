from django.conf.urls import patterns, url

from CalorieCloud.apps.Events import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'/event_creation/', views.eventCreation, name='eventCreation'),
	url(r'^(\d?)/$', views.index, name='index'),
)