from django.shortcuts import get_object_or_404

from businesslogic.models import Slider


#


def get_slider_list() -> list[Slider]:
    return list(Slider.objects.filter(is_active=True))