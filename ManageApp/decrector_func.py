# -*- coding: utf-8 -*-
import json
from functools import wraps

import logging
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseRedirect
from django.http import HttpResponseServerError
from django.shortcuts import redirect

from ManageApp.base_class import GenericResponse, ResInfo, GenericStreamingResponse
from ManageApp.business_exception import BusinessException

method_list = ['GET', 'POST']

logger = logging.getLogger("django")


def generic_response_body(method):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            try:
                check_out = check_request(request, method)
                if check_out == 200:
                    res_info = func(request, *args, **kwargs)
                    return GenericResponse(ResInfo(result=res_info))
                else:
                    return check_out
            except BusinessException as e:
                logger.error(repr(e))
                # build error message
                return GenericResponse(content=ResInfo(res_code=e.code, message=e.message, success=True))
            except Exception as e:
                logger.error(repr(e))
                return GenericResponse(content=ResInfo(res_code=0000, message=e.message, success=True))
        return returned_wrapper

    return decorator


def streaming_response_body(method):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            try:
                check_out = check_request(request, method)
                if check_out == 200:
                    res_info = func(request, *args, **kwargs)
                    return GenericStreamingResponse(res_info)
                else:
                    return check_out
            except Exception as e:
                logger.error(repr(e))
                return HttpResponseServerError()
        return returned_wrapper
    return decorator


def check_request(request, *args):
    """
    验证request以及装饰器参数
    :param request:
    :param args:
    :return:
    """
    if args[0] in method_list and request.method == args[0]:
        return 200
    else:
        return HttpResponseNotAllowed(HttpResponse())
