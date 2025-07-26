from businesslogic.models import News


#


def get_news_list() -> list[News]:
    return list(News.objects.filter(is_active=True))
