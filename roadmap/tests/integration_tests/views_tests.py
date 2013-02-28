"""Tests for the views of the ``roadmap`` app."""
from django.test import TestCase, RequestFactory

from ...views import RoadmapView


class RoadmapViewTestCase(TestCase):
    """Tests for the ``RoadmapView`` view class."""
    def test_anonymous(self):
        """Should be callable when anonymous."""
        req = RequestFactory().get('/')
        resp = RoadmapView.as_view()(req)
        self.assertEqual(resp.status_code, 200)
