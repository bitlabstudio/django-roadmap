"""django-cms app for the ``roadmap`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class RoadmapApp(CMSApp):
    name = _("Roadmap App")
    urls = ["roadmap.urls"]


apphook_pool.register(RoadmapApp)
