from ninja import ModelSchema, Schema

from businesslogic.models import Slider


#


class SliderOutSchema(ModelSchema):

    class Config:
        model = Slider
        model_fields = "__all__"
