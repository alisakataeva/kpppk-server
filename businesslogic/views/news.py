from typing import Optional

from django.shortcuts import get_object_or_404

from businesslogic.models import News


#


def get_news_list() -> list[News]:
    return list(News.objects.filter(is_active=True))


def get_landing_news_list() -> list[News]:
    return list(News.objects.filter(is_active=True))[:4]


def get_news_detail(id: int) -> News:
    return get_object_or_404(News, pk=id)
