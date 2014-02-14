"""Admin classes for the ``roadmap`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from .models import Event, Milestone


class EventAdmin(TranslatableAdmin):
    list_display = ['get_title', 'all_translations', ]

    def get_title(self, obj):
        return obj.title
    get_title.short_description = _('Title')


class MilestoneAdmin(TranslatableAdmin):
    list_display = ['get_name', 'all_translations', ]

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


admin.site.register(Event, EventAdmin)
admin.site.register(Milestone, MilestoneAdmin)
