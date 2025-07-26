from django.http import HttpRequest

from ninja import Router

from common.schemas import BaseJsonResponse
from businesslogic.schemas.response import NewsListResponse, ProgramListResponse
from businesslogic.views.news import get_news_list
from businesslogic.views.program import get_program_list


#


router = Router()


@router.get('/blank', response={200: BaseJsonResponse})
def blank_request(request: HttpRequest):
    return 200, {'code': 'OK', 'message': 'This is blank request!'}


@router.get('/news/list', response={200: NewsListResponse})
def get_news_list_endpoint(request: HttpRequest):
    return 200, {'code': 'OK', 'message': '', 'news_list': get_news_list()}


@router.get('/program/list', response={200: ProgramListResponse})
def get_program_list_endpoint(request: HttpRequest):
    return 200, {'code': 'OK', 'message': '', 'program_list': get_program_list()}
