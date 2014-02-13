"""Models for the ``roadmap`` app."""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from hvad.models import TranslatableModel, TranslatedFields


class Milestone(TranslatableModel):
    """
    A Milestone groups several events on the roadmap.

    :start_date: The date when the implementation of this milestone is
      supposed to be finished. This is mainly used to order the milestones
      on the website.

    """
    class Meta:
        ordering = ('start_date', )

    start_date = models.DateField()

    translations = TranslatedFields(
        name=models.CharField(
            max_length=1024,
            verbose_name=_('Name'),
        )
    )

    def __unicode__(self):
        return self.get_name()

    def get_name(self):
        return self.safe_translation_getter('name', 'Untranslated milestone')


class MilestoneTranslationRenamed(models.Model):
    """
    Translateable fields of a ``Milestone``.

    :milestone: FK to the object this transltation belongs to.
    :name: The name of the Milestone.
    :language: Needed by simple-translation

    """
    # Needed by simple-translation
    milestone = models.ForeignKey(Milestone)
    language = models.CharField(
        max_length=5,
        choices=settings.LANGUAGES
    )

    name = models.CharField(
        max_length=1024,
        verbose_name=_('Name'),
    )


class Event(TranslatableModel):
    """
    An event belongs to a milestone.

    :milestone: FK to the milestone this event belongs to.
    :start_date: The date when the event should be done. This is mainly used to
      order the events on the website.

    """
    class Meta:
        ordering = ('start_date', )

    milestone = models.ForeignKey(
        Milestone,
        verbose_name=_('Milestone'),
        related_name='events',
    )
    start_date = models.DateField(verbose_name=_('Start date'))

    translations = TranslatedFields(
        start_date_text=models.CharField(
            max_length=1024,
            verbose_name=_('Start date text'),
        ),
        title=models.CharField(
            max_length=1024,
            verbose_name=_('Title'),
        ),
        description=models.TextField(
            verbose_name=_('Description'),
            blank=True,
        )
    )

    def __unicode__(self):
        return self.safe_translation_getter(
            'title',
            'Event of {0}'.format(self.milestone))


class EventTranslationRenamed(models.Model):
    """
    Translateable fields of an ``Event``.

    :event: FK to the object this transltation belongs to.
    :language: Needed by simple-translation
    :start_date_text: A description of the start date. For example the start
      date might be 01.01.2013 but we want to display "Q1 2013" on the website.
    :title: A short description of the event.
    :description: An optional long description of the event.

    """
    # needed by simple-translation
    event = models.ForeignKey(Event)
    language = models.CharField(
        max_length=5,
        choices=settings.LANGUAGES
    )

    start_date_text = models.CharField(
        max_length=1024,
        verbose_name=_('Start date text'),
    )

    title = models.CharField(
        max_length=1024,
        verbose_name=_('Title'),
    )

    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
    )
