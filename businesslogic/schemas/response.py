from typing import Optional

from common.schemas import BaseJsonResponse
from .news import NewsListOutSchema, NewsPaginationOutSchema
from .program import ProgramListOutSchema
from .page import PageOutSchema


#


class NewsPaginationResponse(BaseJsonResponse):
    news_pagination: Optional[NewsPaginationOutSchema]


class NewsListResponse(BaseJsonResponse):
    news_list: Optional[list[NewsListOutSchema]]


class NewsDetailResponse(BaseJsonResponse):
    news_detail: Optional[NewsListOutSchema]


#


class ProgramListResponse(BaseJsonResponse):
    program_list: Optional[list[ProgramListOutSchema]]


class ProgramDetailResponse(BaseJsonResponse):
    program_detail: Optional[ProgramListOutSchema]


#


class PageGroupResponse(BaseJsonResponse):
    page_list: Optional[list[PageOutSchema]]


#


class SearchResponse(BaseJsonResponse):
    page_list: Optional[list[PageOutSchema]]
