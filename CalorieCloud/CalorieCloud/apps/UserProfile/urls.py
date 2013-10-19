from django.conf.urls import patterns, url

from CalorieCloud.apps.UserProfile import views
urlpatterns = patterns('',
	url(r'^$', views.profile_page, name='profile_page'),
	url(r'^register', views.register, name='register'),
	url(r'^link_jawbone', views.link_jawbone, name='link_jawbone'),
)