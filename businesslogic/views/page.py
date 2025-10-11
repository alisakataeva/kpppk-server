from django.shortcuts import get_object_or_404

from businesslogic.models import Page


#


def get_page_list_by_group(group: str) -> list[Page]:
    return list(Page.objects.filter(is_active=True, group=group))

