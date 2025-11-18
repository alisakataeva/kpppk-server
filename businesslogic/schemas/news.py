from ninja import ModelSchema, Schema

from businesslogic.models import News


#


class NewsListOutSchema(ModelSchema):

    class Config:
        model = News
        model_fields = "__all__"


class NewsPaginationOutSchema(Schema):
    current_page: int
    num_pages: int
    news_list: list[NewsListOutSchema]
