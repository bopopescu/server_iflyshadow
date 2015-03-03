# -*- coding: utf-8 -*-
__author__ = 'sharp'
import urllib
import time

import simplejson
from httplib2 import Http
from sqlalchemy.orm import sessionmaker
from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.InstagramAccount import *
from getfollow.Module.Utils.Util import *


class InstagramOAuth(object):
    @staticmethod
    def process_oauth():
        if request.method != 'POST':
            return Util.create_response(code=400, error='Error_request_method.')

        # server auth mode
        if 'code' in request.form:
            print request.form.get('code')
            return InstagramOAuth.exchange_for_access_token()
        else:
            print request.form


    @staticmethod
    def exchange_for_access_token():
        if request.method != 'POST':
            return Util.create_response(code=400, error='Error_request_method.')
        # # 1. get code error
        # error = request.args.get('error')
        # if error is not None:
        # error_reason = request.args.get('error_reason')
        # error_description = request.args.get('error_description')
        # return Util.create_response(code=511,
        # error='Get_igm_code_error:' + error + ',' + error_reason + ',' + error_description)

        # 2. get code && exchange access_token

        code = request.form.get('code')

        client_params = {
            "client_id": GET_FOLLOW_CONFIG.CLIENT_ID,
            "client_secret": GET_FOLLOW_CONFIG.CLIENT_SECRET,
            "redirect_uri": GET_FOLLOW_CONFIG.REDIRECT_URI,
            "grant_type": GET_FOLLOW_CONFIG.GRANT_TYPE,
            "code": code
        }
        data = urllib.urlencode(client_params)
        http_object = Http(disable_ssl_certificate_validation=True)
        response, content = http_object.request(GET_FOLLOW_CONFIG.ACCESS_TOKEN_REQUEST_URI, method="POST",
                                                body=data)
        content_json = simplejson.loads(content.decode(), strict=False)
        # 3. exchange access_token error
        if int(response['status']) != 200:
            return Util.create_response(code=int(response['status']),
                                        error='Exchange Access_token error:' + content_json.get(
                                            "error_message", ""))

        # 4. succeed
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

