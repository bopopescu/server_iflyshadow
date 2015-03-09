# -*- coding: utf-8 -*-
__author__ = 'sharp'
import urllib
import time

import simplejson
from httplib2 import Http
from getfollow.Module.Data.InstagramAccount import *
from getfollow.Module.Utils.Util import *


class InstagramOAuth(object):
    @staticmethod
    def process_oauth():
        if request.method != 'POST':
            return Util.create_response(code=400, error='Error_request_method.')
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
        params_decrypted = Util.decrypt(request.form.get('data'))
        content_json = simplejson.loads(params_decrypted, strict=False)
        if 'data_info' in content_json:
            if 'igm_code' in content_json['data_info']:
                # server auth mode
                igm_code = content_json['data_info']['igm_code']
                status, igm_json = InstagramOAuth.exchange_for_access_token(igm_code)
                if status != 200:
                    return Util.create_response(code=status,
                                                error='Exchange Access_token error:' + igm_json.get(
                                                    "error_message", ""))
                else:
                    access_token = content_json['access_token']
                    insta_user_json = content_json['user']
                    igm_account=InstagramAccount()
                    igm_account.save(access_token,insta_user_json)
            else:
                # client auth mode
                return Util.create_response(code=400, error='params format error: no igm code')
        else:
            return Util.create_response(code=400, error='params format error: no data_info')


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



        # 3. succeed
        My_Session = sessionmaker(bind=MYSQL_ENGINE)
        my_session = My_Session()
        access_token = content_json['access_token']
        insta_user = content_json['user']
        print content_json
        try:
            # 4.1 merge MainAccount or add
            main_account = MainAccount(last_access_time=int(time.time() * 1000),
                                       ip_address=request.headers.get('X-Real-Ip', request.remote_addr))
            insta_account_has_existed = my_session.query(InstagramAccount).filter(
                InstagramAccount.uid == insta_user['id']).first()
            if insta_account_has_existed is not None:
                main_account.mid = insta_account_has_existed.mid
                my_session.merge(main_account)
            else:
                my_session.add(main_account)
            my_session.commit()

            # 4.1 merge MainAccount or add
            insta_account = InstagramAccount(mid=main_account.mid, uid=insta_user['id'],
                                             user_name=insta_user['username'],
                                             full_name=insta_user['full_name'], bio=insta_user['bio'],
                                             website=insta_user['website'],
                                             profile_picture=insta_user['profile_picture'],
                                             access_token=access_token)
            if insta_account_has_existed is not None:
                my_session.merge(insta_account)
            else:
                my_session.add(insta_account)
            my_session.commit()
            return Util.create_response(data=content)
        except Exception, e:
            err_info = "OAuth Error %s" % (e.args[0])
            print(err_info)
            return Util.create_response(code=512, error=err_info)

