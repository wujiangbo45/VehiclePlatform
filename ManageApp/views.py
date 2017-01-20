import base64
import json


# Create your views here.
import logging
import os

from django.http import StreamingHttpResponse

import settings
from ManageApp.decrector_func import generic_response_body, streaming_response_body
from MobileMessage.MessageRequest import MessageRequest

logger = logging.getLogger(__name__)


@generic_response_body(method='POST')
def l_list(request):
    b = MessageRequest("1884234882")
    b.send_message()
    return {1: 3}


@streaming_response_body(method='POST')
def test_streaming(request):
    b = open('%s/file_dir/0GP3_OTAFunctionTest0112.bin' % settings.PROJECT_DIR, 'r')
    return b

