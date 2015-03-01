# -*- coding: utf-8 -*-
__author__ = 'sharp'
from json import *

from flask import *
from Crypto.Cipher import AES
from Crypto import Random
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
        unpad = lambda s: s[0:-ord(s[-1])]
        print(SECURITY_CONFIG.AES_KEY)
        cipher = AES.new(SECURITY_CONFIG.AES_KEY)
        encrypted = cipher.encrypt(pad(data)).encode('hex')
        print encrypted  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'

        decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
        print decrypted  # will be 'to be encrypted'

    @staticmethod
    def decrypt(data):
        block_size = AES.block_size
        pad = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
        unpad = lambda s: s[0:-ord(s[-1])]
        print(SECURITY_CONFIG.AES_KEY)
        cipher = AES.new(SECURITY_CONFIG.AES_KEY)
        encrypted = cipher.encrypt(pad(data)).encode('hex')
        print encrypted  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'

        decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
        print decrypted  # will be 'to be encrypted'

