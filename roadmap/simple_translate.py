"""Registering translated models for the ``roadmap`` app."""
from simple_translation.translation_pool import translation_pool

from .models import Event, EventTranslation, Milestone, MilestoneTranslation


translation_pool.register_translation(Event, EventTranslation)
translation_pool.register_translation(Milestone, MilestoneTranslation)
