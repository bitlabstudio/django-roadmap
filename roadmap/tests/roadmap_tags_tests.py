"""Tests for the templatetags of the ``roadmap`` app."""
from django.test import TestCase

from ..templatetags.roadmap_tags import get_roadmap_events
from .factories import EventFactory


class GetRoadmapEventsTestCase(TestCase):
    """Tests for the ``get_roadmap_events`` templatetag."""
    def test_tag(self):
        EventFactory()
        EventFactory()
        EventFactory()
        result = get_roadmap_events(amount=2)
        self.assertEqual(result.count(), 2)
