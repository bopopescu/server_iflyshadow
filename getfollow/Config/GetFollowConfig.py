# -*- coding: utf-8 -*-
import base64

from yaml import load

from Consts import *


class GetFollowConfig():
    KEY_GET_FOLLOW = "Get_Follow"
    KEY_INSTAGRAM = "Instagram"
    KEY_CLIENT_ID = "Client_ID"
    KEY_CLIENT_SECRET = "Client_Secret"
    KEY_REDIRECT_URI = "Redirect_Uri"
    KEY_ACCESS_TOKEN_REQUEST_URI = "Access_Token_Request_URL"

    CLIENT_ID = ""
    CLIENT_SECRET = ""
    REDIRECT_URI = ""
    ACCESS_TOKEN_REQUEST_URI = ""
    GRANT_TYPE = "authorization_code"

    def __init__(self):
        self.load_config()

    def load_config(self):
        if len(self.CLIENT_ID) == 0 or len(self.CLIENT_SECRET) == 0 or len(self.REDIRECT_URI) == 0 or len(
                self.ACCESS_TOKEN_REQUEST_URI) == 0:
            # data map
            data_map = dict()
            try:
                f = open(GLOBAL_CONFIG_FILE)
                data_map = load(f)
                f.close()
            except Exception, e:
                print "Error %s" % (e.args[0])

            # 1. Get Follow
            try:
                get_follow_dic = data_map[self.KEY_GET_FOLLOW]
                get_follow_instagram_dic = get_follow_dic[self.KEY_INSTAGRAM]
                self.CLIENT_ID = base64.b64decode(get_follow_instagram_dic[self.KEY_CLIENT_ID])
                self.CLIENT_SECRET = base64.b64decode(get_follow_instagram_dic[self.KEY_CLIENT_SECRET])
                self.REDIRECT_URI = base64.b64decode(get_follow_instagram_dic[self.KEY_REDIRECT_URI])
                self.ACCESS_TOKEN_REQUEST_URI = base64.b64decode(
                    get_follow_instagram_dic[self.KEY_ACCESS_TOKEN_REQUEST_URI])
            except Exception, e:
                print "error %s" % (e.args[0])

    def set_config(self, data_map):
        print "Get Follow Config ---"
        print self.CLIENT_ID, self.CLIENT_SECRET,self.REDIRECT_URI,self.ACCESS_TOKEN_REQUEST_URI
        self.CLIENT_ID = raw_input(self.KEY_CLIENT_ID + ":")  # "ideastraysql.cvl6s0er3syb.us-west-2.rds.amazonaws.com"
        self.CLIENT_SECRET = raw_input(self.KEY_CLIENT_SECRET + ":")
        self.REDIRECT_URI = raw_input(self.KEY_REDIRECT_URI + ":")
        self.ACCESS_TOKEN_REQUEST_URI = raw_input(self.KEY_ACCESS_TOKEN_REQUEST_URI + ":")

        if len(self.CLIENT_ID) > 0 or len(self.CLIENT_SECRET) > 0 or len(self.REDIRECT_URI) or len(
                self.ACCESS_TOKEN_REQUEST_URI) > 0:
            get_follow_instagram_dic = dict()
            get_follow_instagram_dic[self.KEY_CLIENT_ID] = base64.b64encode(self.CLIENT_ID)
            get_follow_instagram_dic[self.KEY_CLIENT_SECRET] = base64.b64encode(self.CLIENT_SECRET)
            get_follow_instagram_dic[self.KEY_REDIRECT_URI] = base64.b64encode(self.REDIRECT_URI)
            get_follow_instagram_dic[self.KEY_ACCESS_TOKEN_REQUEST_URI] = base64.b64encode(
                self.ACCESS_TOKEN_REQUEST_URI)
            get_follow_dic = dict()
            get_follow_dic[self.KEY_INSTAGRAM] = get_follow_instagram_dic
            data_map[self.KEY_GET_FOLLOW] = get_follow_dic



