# -*- coding: utf-8 -*-
import base64

from yaml import load

from Consts import *


class MySqlConfig():
    KEY_MYSQL = "MySql"
    KEY_HOST = "Host"
    KEY_USER = "User"
    KEY_PASSWORD = "Password"
    KEY_SCHEMA = "Schema"

    HOST = ""
    USER = ""
    PASSWORD = ""
    SCHEMA = "test"

    def __init__(self):
        self.load_config()

    def load_config(self):
        if len(self.HOST) == 0 or len(self.USER) == 0 or len(self.PASSWORD) == 0:
            # data map
            data_map = dict()
            try:
                f = open(GLOBAL_CONFIG_FILE)
                data_map = load(f)
                f.close()
            except Exception, e:
                print "Error %s" % (e.args[0])

            # 1. MySql
            try:
                mysql_dic = data_map[self.KEY_MYSQL]
                self.HOST = base64.b64decode(mysql_dic[self.KEY_HOST])
                self.USER = base64.b64decode(mysql_dic[self.KEY_USER])
                self.PASSWORD = base64.b64decode(mysql_dic[self.KEY_PASSWORD])
                self.SCHEMA = base64.b64decode(mysql_dic[self.KEY_SCHEMA])
            except Exception, e:
                print "error %s" % (e.args[0])

    def set_config(self, data_map):
        print "Mysql Config ---"
        self.HOST = raw_input(self.KEY_HOST + ":")  # "ideastraysql.cvl6s0er3syb.us-west-2.rds.amazonaws.com"
        self.USER = raw_input(self.KEY_USER + ":")
        self.PASSWORD = raw_input(self.KEY_PASSWORD + ":")
        self.SCHEMA = raw_input(self.KEY_SCHEMA + ":")

        if len(self.HOST) > 0 or len(self.USER) > 0 or len(self.PASSWORD):
            mysql_dic = dict()
            mysql_dic[self.KEY_HOST] = base64.b64encode(self.HOST)
            mysql_dic[self.KEY_USER] = base64.b64encode(self.USER)
            mysql_dic[self.KEY_PASSWORD] = base64.b64encode(self.PASSWORD)
            mysql_dic[self.KEY_SCHEMA] = base64.b64encode(self.SCHEMA)
            data_map[self.KEY_MYSQL] = mysql_dic



