"""Admin classes for the ``roadmap`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from .models import Event, Milestone


class EventAdmin(TranslationAdmin):
    list_display = ['title', 'languages', ]

    def title(self, obj):
        lang = get_language()
        trans = get_preferred_translation_from_lang(obj, lang)
        return trans.title
    title.short_description = _('Title')


class MilestoneAdmin(TranslationAdmin):
    list_display = ['name', 'languages', ]

    def name(self, obj):
        lang = get_language()
        trans = get_preferred_translation_from_lang(obj, lang)
        return trans.name
    name.short_description = _('Name')


admin.site.register(Event, EventAdmin)
admin.site.register(Milestone, MilestoneAdmin)
