from django.conf.urls import patterns, url

from CalorieCloud.apps.Transactions import views
urlpatterns = patterns('',
	url(r'^$', views.donation, name='donation'),
)