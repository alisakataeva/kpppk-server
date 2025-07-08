from django.http import HttpRequest

from ninja import Router

from common.schemas import BaseJsonResponse


#


router = Router()


@router.get('/blank', response={200: BaseJsonResponse})
def blank_request(request: HttpRequest):
    return 200, {'code': 'OK', 'message': 'This is blank request!'}
