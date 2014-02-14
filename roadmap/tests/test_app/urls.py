"""URLs for the ``roadmap.tests.test_app`` app."""
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^roadmap/', include('roadmap.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cms.urls')),
)
