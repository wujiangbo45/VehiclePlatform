#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-1-17 下午1:09
# @Author  : 武江波
# @Site    : 
# @File    : MessageRequest.py
# @Software: PyCharm
import json
import urllib2

import settings
from ManageApp.base_class import ResInfo
from MobileMessage.HttpRequestBase import HttpJsonRequest
from utils import to_json


class MessageRequest(HttpJsonRequest):

    """
        发送短信请求
    """
    def __init__(self, mobile_phone_number, *args, **kwargs):
        super(MessageRequest, self).__init__(*args, **kwargs)
        self.mobile_phone_number = mobile_phone_number
        self.headers.update({"X-LC-Id": settings.X_LC_ID,
                             "X-LC-Key": settings.X_LC_KEY})

    def send_message(self):
        """
        send verity code to mobile phone
        :return:
        """
        self.url = settings.MESSAGE_URL
        # update headers

        self.data = {"mobilePhoneNumber": self.mobile_phone_number,
                     "ttl": settings.TTL,
                     "name": settings.MESSAGE_NAME,
                     "op": settings.MESSAGE_OP}
        return self.post()

    def post(self):
        """
        向短信服务器发送请求
        :return:
        """
        try:
            print self.get_post_response()
            # send success and set default message
            self.res = {"code": "200", "error": ""}
            res_info = ResInfo()
        except urllib2.HTTPError:
            dict_res = json.loads(self.res)
            res_info = ResInfo(res_code=dict_res['code'], success=False, message=dict_res['error'])
        finally:
            return to_json(res_info.get_dictionary())

    def verify_mobile(self, message_code):
        """
        verify code from mobile received
        :return:
        """
        self.url = '{0}{1}?mobilePhoneNumber={2}'.\
            format(settings.MESSAGE_VERIFY_URL, message_code, self.mobile_phone_number)
        return self.post()


if __name__ == "__main__":
    b = MessageRequest("1884234882")
    print b.send_message()
    # print b.verify_mobile(699153)
