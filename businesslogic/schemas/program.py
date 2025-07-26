from ninja import ModelSchema, Schema

from businesslogic.models import Program


#


class ProgramListOutSchema(ModelSchema):

    class Config:
        model = Program
        model_fields = "__all__"
