from typing import Optional

from ninja import Schema

from .news import NewsListOutSchema
from .program import ProgramListOutSchema


#


class GetNewsDetailRequest(Schema):
    news_id: int


class GetNewsListRequest(Schema):
    truncated: Optional[int]


class GetNewsPaginationRequest(Schema):
    page: int


#


class GetProgramDetailRequest(Schema):
    program_id: int


class GetProgramListRequest(Schema):
    truncated: Optional[int]


#


class GetPageGroupRequest(Schema):
    group: str


#


class SearchRequest(Schema):
    searchstr: str


#


class EmailFeedbackRequest(Schema):
    email: str
    name: str
    message: str

