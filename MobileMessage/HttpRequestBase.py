#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-1-16 下午2:44
# @Author  : 武江波
# @Site    : 
# @File    : HttpRequestBase.py
# @Software: PyCharm

import urllib
import urllib2
import json


from Const import CONTENT_TYPE_JSON


class HttpRequestBase(object):
    """
    """

    def __init__(self, url=None, data=None):
        self.url = url
        self._headers = {}
        self._data = data
        self._response = None

        self._code = None
        self._res = None

    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        """
        build headers for request
        :param value:
        :return:
        """
        # value must be dictionary
        if value and isinstance(value, dict):
            # set header to headers
            for key in value.keys():
                self._headers[key] = value[key]
        self._headers['Accept'] = 'application/json;charset=UTF-8'

    @property
    def opener(self):
        pass

    @opener.getter
    def opener(self):
        opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1), urllib2.HTTPSHandler(debuglevel=1))
        return opener

    def build_post_request(self):
        return urllib2.Request(self.url, self.data, self.headers)

    def get_request(self):
        urllib.urlopen('%s?%s' % self.url, self.data)

    def post_request(self):
        post_request = self.build_post_request()
        self._response = self.opener.open(post_request)
        # self._response = urllib2.urlopen(post_request)

    def get_post_response(self):
        try:
            self.post_request()
            self._code = self._response.code
            self._res = self._response.read()
        except urllib2.HTTPError as e:
            # get exception message
            self._code = e.code
            self._res = e.read()
            if self._res is not None or self._res == '':
                raise e
        return self._res


class HttpJsonRequest(HttpRequestBase):
    """
        发出json请求
    """
    def __init__(self, *args, **kwargs):
        super(HttpJsonRequest, self).__init__(*args, **kwargs)
        self.data = self.data
        self.headers = {'Content-Type': '%s;charset=UTF-8' % CONTENT_TYPE_JSON}

    @HttpRequestBase.data.setter
    def data(self, value):
        self._data = json.dumps(value)

if __name__ == "__main__":
    print HttpJsonRequest(url="http://localhost:8000/test/1/",
                          data={"carId": "33333"}).get_post_response()
