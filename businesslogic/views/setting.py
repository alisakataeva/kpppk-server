from django.shortcuts import get_object_or_404

from businesslogic.models import SiteSetting


#


def get_settings() -> list[SiteSetting]:
    return list(SiteSetting.objects.all())
