# -*- coding: utf-8 -*-
import json
from functools import wraps

import logging
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from ManageApp.base_class import GenericResponse, ResInfo
from ManageApp.business_exception import BusinessException

method_list = ['GET', 'POST']

logger = logging.getLogger("django")


def generic_response_body(method):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            try:
                if method in method_list and request.method == method:
                    res_info = func(request, *args, **kwargs)
                    return GenericResponse(ResInfo(result=res_info))
                else:
                    return HttpResponseNotAllowed(HttpResponse())
            except BusinessException as e:
                logger.error(repr(e))
                # build error message
                return GenericResponse(content=ResInfo(res_code=e.code, message=e.message, success=True))
            except Exception as e:
                logger.error(repr(e))
                return GenericResponse(content=ResInfo(res_code=0000, message=e.message, success=True))
        return returned_wrapper

    return decorator
