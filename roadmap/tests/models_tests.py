"""Tests for the models of the ``roadmap`` app."""
from django.test import TestCase

from .factories import EventFactory, MilestoneFactory


class MilestoneTestCase(TestCase):
    """Tests for the ``Milestone`` model."""
    def test_model(self):
        """Should be able to instantiate and save."""
        obj = MilestoneFactory()
        self.assertTrue(obj.pk)


class EventTestCase(TestCase):
    """Tests for the ``Event`` model."""
    def test_model(self):
        """Should be able to instantiate and save."""
        obj = EventFactory()
        self.assertTrue(obj.pk)
