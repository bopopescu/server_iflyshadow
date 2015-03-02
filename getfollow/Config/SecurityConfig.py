# -*- coding: utf-8 -*-
import base64

from yaml import load
from Consts import *


class SecurityConfig():
    KEY_SECURITY = "Security"
    KEY_AES_KEY = "AES_Key"

    AES_KEY = ""

    def __init__(self):
        self.load_config()

    def load_config(self):
        if len(self.AES_KEY) == 0:
            # data map
            data_map = dict()
            try:
                f = open(GLOBAL_CONFIG_FILE)
                data_map = load(f)
                f.close()
            except Exception, e:
                print "Error %s" % (e.args[0])

            # 1. SecurityConfig
            try:
                security_dic = data_map[self.KEY_SECURITY]
                self.AES_KEY = base64.b64decode(security_dic[self.KEY_AES_KEY])
            except Exception, e:
                print "error %s" % (e.args[0])

    def set_config(self, data_map):
        print "Security Config ---"
        print self.AES_KEY #*icanfly!(@*#&$^
        self.AES_KEY = raw_input(self.KEY_AES_KEY + ":")

        if len(self.AES_KEY) > 0:
            security_dic = dict()
            security_dic[self.KEY_AES_KEY] = base64.b64encode(self.AES_KEY)
            data_map[self.KEY_SECURITY] = security_dic



