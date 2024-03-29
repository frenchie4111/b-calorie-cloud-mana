from django.conf.urls import patterns, url

from CalorieCloud.apps.UserProfile import views
urlpatterns = patterns('',
	url(r'^$', views.profile_page, name='profile_page'),
	url(r'^(\d?)/$', views.profile_page, name='profile_page'),
	url(r'^login', views.login, name='login'),
	url(r'^logout', views.logout, name='logout'),
	url(r'^register', views.register, name='register'),
	url(r'^link_jawbone', views.link_jawbone, name='link_jawbone'),
	url(r'^update_calories', views.update_calories, name='update_calories'),
)