from typing import Optional

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from businesslogic.models import News
from businesslogic.schemas.news import NewsPaginationOutSchema


#


def get_news_list() -> list[News]:
    return list(News.objects.filter(is_active=True))


def get_news_pagination(page: int) -> NewsPaginationOutSchema:
    p = Paginator(News.objects.all(), 5)
    return {
        "current_page": page,
        "num_pages": p.num_pages,
        "news_list": list(p.page(page).object_list)
    }


def get_landing_news_list() -> list[News]:
    return list(News.objects.filter(is_active=True))[:4]


def get_news_detail(id: int) -> News:
    return get_object_or_404(News, pk=id)
