from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CalorieCloud.views.home', name='home'),
    # url(r'^CalorieCloud/', include('CalorieCloud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'CalorieCloud.core.views.home_page', name='home_page'),
    url(r'^user/', include('CalorieCloud.apps.UserProfile.urls')),
    url(r'^transaction/', include('CalorieCloud.apps.Transactions.urls')),
<<<<<<< HEAD
    url(r'^events/', include('CalorieCloud.apps.Events.urls')),
=======
    url(r'^groups/', include('CalorieCloud.apps.Groups.urls')),
>>>>>>> b66717940f5a7c5921bcafdbe0378f1e2d699d2e
)
