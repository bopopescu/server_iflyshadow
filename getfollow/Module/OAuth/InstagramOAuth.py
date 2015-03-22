# -*- coding: utf-8 -*-
__author__ = 'sharp'
import urllib

import simplejson
from httplib2 import Http
from getfollow.Module.Data.InstagramAccount import *
from getfollow.Module.Utils.Util import *
import time


class InstagramOAuth(object):
    @staticmethod
    def process_oauth():
        if request.method != 'POST':
            return Util.create_response(code=400, error='Error_request_method.')

        params_decrypted = Util.decrypt(request.form.get('data'))
        content_json = simplejson.loads(params_decrypted, strict=False)

        if 'data_info' not in content_json:
            return Util.create_response(code=400, error='params format error: no data_info')
        if 'igm_code' not in content_json['data_info']:
            # client auth mode
            return Util.create_response(code=400, error='params format error: no igm code in data_info')
        if 'bundle_info' not in content_json:
            return Util.create_response(code=400, error='params format error: no bundle_info')

        # server auth mode:exchange_for_access_token
        igm_code = content_json['data_info']['igm_code']
        status, igm_json = InstagramOAuth.exchange_for_access_token(igm_code)
        if status != 200:
            return Util.create_response(code=status,
                                        error='Exchange Access_token error:' + igm_json.get(
                                            "error_message", ""))

        # 1. save MainAccount && InstagramAccount
        igm_user = content_json['data_info']['igm_user']
        igm_password = content_json['data_info']['igm_password']
        access_token = igm_json['access_token']
        igm_user_json = igm_json['user']
        igm_account = InstagramAccount()
        flag, code, error = igm_account.update_to_db(igm_user_json=igm_user_json,
                                                     access_token=access_token,
                                                     igm_user=igm_user,
                                                     igm_password=igm_password)
        if not flag:
            return Util.create_response(code=code, error=error)

        # 2. save BundleUser
        bundle = BundleUser()
        flag, code, error = bundle.update_to_db(mid=igm_account.mid, uid=igm_account.uid,
                                                bundle_info_json=content_json['bundle_info'], is_login=True)
        if not flag:
            return Util.create_response(code=code, error=error)

        igm_json['session_id'] = bundle.session_id
        igm_json['server_time'] = int(time.time() * 1000)
        igm_json['mid'] = igm_account.mid
        print igm_json
        return Util.create_response(data=igm_json)


    @staticmethod
    def exchange_for_access_token(igm_code):
        # 1. get code && exchange access_token

        client_params = {
            "client_id": GET_FOLLOW_CONFIG.CLIENT_ID,
            "client_secret": GET_FOLLOW_CONFIG.CLIENT_SECRET,
            "redirect_uri": GET_FOLLOW_CONFIG.REDIRECT_URI,
            "grant_type": GET_FOLLOW_CONFIG.GRANT_TYPE,
            "code": igm_code
        }
        data = urllib.urlencode(client_params)
        http_object = Http(disable_ssl_certificate_validation=True)
        response, content = http_object.request(GET_FOLLOW_CONFIG.ACCESS_TOKEN_REQUEST_URI, method="POST",
                                                body=data)
        content_json = simplejson.loads(content.decode(), strict=False)
        return int(response['status']), content_json

        # {
        # "bundle_info" : {
        # "mid":
        # "uid":
        #
        # "session_id" : "",
        # "device_token" : "",
        #
        # "bundle_id" : "com.ideastray.GetFollow",
        # "bundle_version" : "1",
        #
        # "locale_identifier" : "en_US",
        # "preferred_language" : "en",
        #
        # "device_os_name" : "iPhone OS",
        # "device_os_version" : "8.1",
        # "device_model" : "Simulator",
        #
        # "latitude":
        # "longitude":
        # },
        # "data_info" : {
        # "igm_user" : "sharpidea",
        # "igm_code" : "37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f",
        # "igm_password" : "013513jv"
        # }
        # }


        # {
        # "session_id": ""
        # "access_token": "37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f",
        # "user": {
        # "username": "sharpidea",
        # "bio": "From\\nTesr\\nHaha",
        # "website": "http:\\/\\/test.com.cn",
        # "profile_picture": "https:\\/\\/instagramimages-a.akamaihd.net\\/profiles\\/profile_37004920_75sq_1399257924.jpg",
        # "full_name": "JIABO",
        #     "id": "37004920"
        # }
