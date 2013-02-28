"""Templatetags for the buildee project."""
from django import template

from ..models import Event


register = template.Library()


@register.assignment_tag
def get_roadmap_events(amount=5):
    """
    Returns the next upcoming roadmap events.

    :param amount: The number of events that should be returned.

    """
    qs = Event.objects.all().order_by('start_date')[:amount]
    return qs
