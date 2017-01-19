#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-1-17 下午4:10
# @Author  : 武江波
# @Site    : 
# @File    : utils.py
# @Software: PyCharm
import json


def to_json(dic_str):
    """

    :param dict:
    :return:
    """
    return json.dumps(dic_str, indent=4, ensure_ascii=False)