"""Views for the ``roadmap`` app."""
from django.views.generic import ListView

from .models import Milestone


class RoadmapView(ListView):
    model = Milestone
    queryset = Milestone.objects.all()
