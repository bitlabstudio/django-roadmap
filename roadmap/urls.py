"""URLs for the ``roadmap`` app."""
from django.conf.urls import patterns, url

from .views import RoadmapView


urlpatterns = patterns(
    '',
    url(r'^$',
        RoadmapView.as_view(),
        name='roadmap_view'),
)
