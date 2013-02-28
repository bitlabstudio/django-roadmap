"""Factories for the ``roadmap`` app."""
from django.utils.timezone import now

import factory

from ..models import Event, EventTranslation, Milestone, MilestoneTranslation


class MilestoneFactory(factory.Factory):
    FACTORY_FOR = Milestone

    start_date = factory.LazyAttribute(lambda x: now())


class MilestoneTranslationFactoryBase(factory.Factory):
    FACTORY_FOR = MilestoneTranslation

    milestone = factory.SubFactory(MilestoneFactory)


class MilestoneTranslationENFactory(MilestoneTranslationFactoryBase):
    name = 'A Milestone'
    language = 'en'


class MilestoneTranslationDEFactory(MilestoneTranslationFactoryBase):
    name = 'Ein Meilenstein'
    language = 'de'


class EventFactory(factory.Factory):
    FACTORY_FOR = Event

    milestone = factory.SubFactory(MilestoneFactory)
    start_date = factory.LazyAttribute(lambda x: now())


class EventTranslationFactoryBase(factory.Factory):
    FACTORY_FOR = EventTranslation

    event = factory.SubFactory(EventFactory)


class EventTranslationENFactory(EventTranslationFactoryBase):
    start_date_text = 'Very soon'
    title = 'An event'
    language = 'en'


class EventTranslationDEFactory(EventTranslationFactoryBase):
    start_date_text = 'Sehr bald'
    title = 'Ein Event'
    language = 'de'
