import requests, json
from django.utils.decorators import method_decorator
from django.views import View
from django.db import models
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging
from Apps.users.models import User
logger = logging.getLogger(__name__)




class BaseAPIView(View):
    response = None

    class Response:
        status_code = settings.API['unknown']
        status_txt = settings.API_CODE_MSG[settings.API['unknown']]
        data = []

        def as_dict(self):
            self.status_txt = settings.API_CODE_MSG[self.status_code]
            return {'status_code': self.status_code, 'status_txt': self.status_txt, 'data': self.data}

    def __init__(self, **kwargs):
        super(BaseAPIView, self).__init__(**kwargs)
        self.response = self.Response()

    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseAPIView, self).dispatch(*args, **kwargs)



