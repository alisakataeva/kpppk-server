from ninja import ModelSchema, Schema

from businesslogic.models import News


#


class NewsListOutSchema(ModelSchema):

    class Config:
        model = News
        model_fields = "__all__"
