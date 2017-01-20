# -*- coding: utf-8 -*-
import base64
import json

import logging
from django.http import HttpResponse
from django.http import StreamingHttpResponse

from settings import CHAR_SET
from utils import to_json

logger = logging.getLogger("django")


class ResInfo(object):
    # return result class
    def __init__(self, res_code=200, success=True, message=u'请求成功', result=None):
        self.res_code = res_code
        self.success = success
        self.message = message
        self.result = result

    def __unicode__(self):
        return u'%s' % self.message

    def get_dictionary(self):
        return {'res_code': self.res_code,
                'success': self.success,
                'message': self.message,
                'result': self.result}


class GenericResponse(HttpResponse):

    # cast content to json type
    def __init__(self, content=ResInfo()):
        super(GenericResponse, self).__init__(content_type="application/json", charset=CHAR_SET)
        self.content = to_json(content.get_dictionary())
        logger.info(self.content)


class GenericStreamingResponse(StreamingHttpResponse):

    def __init__(self, content):
        super(GenericStreamingResponse, self).__init__(content_type="octet-stream")
        self.streaming_content = self.file_stream(content)

    @staticmethod
    def file_stream(file_stream):
        for c in file_stream:
            yield base64.b64encode(c)
