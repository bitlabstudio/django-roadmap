"""URLs for the ``roadmap.tests.test_app`` app."""
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'', include('roadmap.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
