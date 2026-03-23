from ninja import ModelSchema, Schema

from businesslogic.models import SiteSetting


#


class SettingOutSchema(ModelSchema):

    class Config:
        model = SiteSetting
        model_fields = "__all__"
