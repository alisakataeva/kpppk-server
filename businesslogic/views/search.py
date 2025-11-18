from django.db import connection
from django.shortcuts import get_object_or_404

from businesslogic.models import Page


#


def page_fulltext_search(searchstr: str) -> list[Page]:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM businesslogic_page WHERE MATCH(title, content)
            AGAINST(%s IN NATURAL LANGUAGE MODE)
        """, [searchstr])
        res = cursor.fetchall()
    models = []
    for p in res:
        result_page = Page(
            id=p[0],
            code=p[1],
            url=p[2],
            group=p[3],
            title=p[4],
            content=p[5],
            order=p[6],
            created_at=p[7],
            is_active=p[8],
            group_name=p[9]
        )
        models.append(result_page)
    return models

