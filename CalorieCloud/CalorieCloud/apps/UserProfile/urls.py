from django.conf.urls import patterns, url

from CalorieCloud.apps.UserProfile import views
urlpatterns = patterns('',
	url(r'^$', views.profile_page, name='profile_page'),
)