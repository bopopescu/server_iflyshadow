# -*- coding: utf-8 -*-
__author__ = 'sharp'
from json import *

from flask import *
from Crypto.Cipher import AES
from getfollow.Config.Consts import *

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

    @staticmethod
    def encrypt(data):
        block_size = AES.block_size
        pad = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
        cipher = AES.new(SECURITY_CONFIG.AES_KEY)
        return cipher.encrypt(pad(data)).encode('hex')

    @staticmethod
    def decrypt(data):
        unpad = lambda s: s[0:-ord(s[-1])]
        cipher = AES.new(SECURITY_CONFIG.AES_KEY)
        return unpad(cipher.decrypt(data.decode('hex')))

