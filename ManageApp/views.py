import json


# Create your views here.
import logging
from django.http import StreamingHttpResponse

from ManageApp.decrector_func import generic_response_body
from MobileMessage.MessageRequest import MessageRequest

logger = logging.getLogger(__name__)


@generic_response_body(method='POST')
def l_list(request):
    b = MessageRequest("1884234882")
    b.send_message()
    return {1: 3}




