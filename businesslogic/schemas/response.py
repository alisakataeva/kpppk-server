from typing import Optional

from common.schemas import BaseJsonResponse
from .news import NewsListOutSchema
from .program import ProgramListOutSchema


#


class NewsListResponse(BaseJsonResponse):
    news_list: Optional[list[NewsListOutSchema]]


class ProgramListResponse(BaseJsonResponse):
    program_list: Optional[list[ProgramListOutSchema]]

