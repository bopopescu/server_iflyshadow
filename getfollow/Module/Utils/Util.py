# -*- coding: utf-8 -*-
__author__ = 'sharp'
from json import *

from flask import *


class Util(object):
    @staticmethod
    def create_response(code=200, data=None, error=None):
        response_dict = dict()
        response_dict['code'] = code
        if code != 200:
            if error is not None:
                response_dict['data'] = error
        else:
            if data is not None:
                try:
                    response_dict['data'] = JSONDecoder().decode(data)
                except ValueError:
                    response_dict['data'] = data
        return make_response(jsonify(response_dict), code)