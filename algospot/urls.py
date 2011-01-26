from django.conf.urls.defaults import *
from django.conf import settings
import django.contrib.admindocs
import registration
import staticfiles
import judge

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^algospot/', include('algospot.foo.urls')),
    (r'^judge/', include('judge.urls')),

    # django-registration
    (r'^accounts/', include('registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include('admin.site.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('', (r'', include("staticfiles.urls")))
