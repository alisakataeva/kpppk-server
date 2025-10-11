from ninja import ModelSchema, Schema

from businesslogic.models import Page


#


class PageOutSchema(ModelSchema):

    class Config:
        model = Page
        model_fields = "__all__"
