from django.http import HttpRequest

import time

from ninja import Router

from common.schemas import BaseJsonResponse
from businesslogic.schemas.request import (
    GetNewsDetailRequest, GetNewsListRequest, \
    GetProgramDetailRequest, GetProgramListRequest, \
    GetPageGroupRequest
)
from businesslogic.schemas.response import (
    NewsListResponse, NewsDetailResponse, \
    ProgramListResponse, ProgramDetailResponse, \
    PageGroupResponse
)
from businesslogic.views.news import get_news_list, get_news_detail, get_landing_news_list
from businesslogic.views.program import get_program_list, get_program_detail, get_landing_program_list
from businesslogic.views.page import get_page_list_by_group
from businesslogic.views.other import send_feedback_email


#


router = Router()


@router.get('/blank', response={200: BaseJsonResponse})
def blank_request(request: HttpRequest):
    return 200, {'code': 'OK', 'message': 'This is blank request!'}


#


@router.post('/news/list', response={200: NewsListResponse})
def get_news_list_endpoint(request: HttpRequest):
    return 200, {'code': 'OK', 'message': '', 'news_list': get_news_list()}


@router.post('/news/landing-list', response={200: NewsListResponse})
def get_news_landing_list_endpoint(request: HttpRequest):
    return 200, {'code': 'OK', 'message': '', 'news_list': get_landing_news_list()}


@router.post('/news/detail', response={200: NewsDetailResponse})
def get_news_detail_endpoint(request: HttpRequest, request_data: GetNewsDetailRequest):
    return 200, {'code': 'OK', 'message': '', 'news_detail': get_news_detail(request_data.news_id)}


#


@router.post('/program/list', response={200: ProgramListResponse})
def get_program_list_endpoint(request: HttpRequest):
    raise Exception('pupupu')
    return 200, {'code': 'OK', 'message': '', 'program_list': get_program_list()}


@router.post('/program/landing-list', response={200: ProgramListResponse})
def get_program_landing_list_endpoint(request: HttpRequest):
    return 200, {'code': 'OK', 'message': '', 'program_list': get_landing_program_list()}


@router.post('/program/detail', response={200: ProgramDetailResponse})
def get_program_detail_endpoint(request: HttpRequest, request_data: GetProgramDetailRequest):
    return 200, {'code': 'OK', 'message': '', 'program_detail': get_program_detail(request_data.program_id)}


#


@router.post('/page-group/list', response={200: PageGroupResponse})
def get_page_group_endpoint(request: HttpRequest, request_data: GetPageGroupRequest):
    return 200, {'code': 'OK', 'message': '', 'page_list': get_page_list_by_group(request_data.group)}


#


@router.post('/send-feedback-email', response={200: BaseJsonResponse})
def send_feedback_email_endpoint(request: HttpRequest):
    try:
        send_feedback_email()
        return 200, {'code': 'OK', 'message': 'Email was sent successfully'}
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e)}