"""Factories for the ``roadmap`` app."""
from django.utils.timezone import now

import factory
from django_libs.tests.factories import HvadFactoryMixin

from ..models import Event, Milestone


class MilestoneFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    FACTORY_FOR = Milestone

    start_date = factory.LazyAttribute(lambda x: now())
    name = factory.Sequence(lambda n: 'name {0}'.format(n))


class EventFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    FACTORY_FOR = Event

    milestone = factory.SubFactory(MilestoneFactory)
    start_date = factory.LazyAttribute(lambda x: now())
    title = factory.Sequence(lambda n: 'title {0}'.format(n))
