# -*- coding: utf-8 -*-
__author__ = 'sharp'
import urllib
import time

import simplejson
from httplib2 import Http
from getfollow.Config.Consts import *
from sqlalchemy.orm import sessionmaker
from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.InstagramAccount import *
from getfollow.Module.Utils.Util import *


class InstagramOAuth(object):
    @staticmethod
    def exchange_for_access_token():
        print("request.method:" + request.method)
        if request.method != 'GET':
            return Util.create_response(code=400, error='Error_request_method.')
        # 1. get code error
        error = request.args.get('error')
        if error is not None:
            error_reason = request.args.get('error_reason')
            error_description = request.args.get('error_description')
            return Util.create_response(code=511,
                                        error='Get_igm_code_error:' + error + ',' + error_reason + ',' + error_description)

        # 2. get code && exchange access_token
        code = request.args.get('code')
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

        parsed_content = simplejson.loads(content.decode(), strict=False)
        # 3. exchange access_token error
        if int(response['status']) != 200:
            return Util.create_response(code=int(response['status']),
                                        error='Exchange Access_token error:' + parsed_content.get(
                                            "error_message", ""))

        # 4. succeed
        Session = sessionmaker(bind=MYSQL_ENGINE)
        session = Session()
        access_token = parsed_content['access_token']
        insta_user = parsed_content['user']
        print parsed_content
        try:
            # 4.1 merge MainAccount or add
            main_account = MainAccount(last_access_time=int(time.time() * 1000), ip_address=request.remote_addr)
            insta_account_has_existed = session.query(InstagramAccount).filter(
                InstagramAccount.uid == insta_user['id']).first()
            if insta_account_has_existed is not None:
                main_account.mid = insta_account_has_existed.mid
                session.merge(main_account)
            else:
                session.add(main_account)
            session.commit()

            # 4.1 merge MainAccount or add
            insta_account = InstagramAccount(mid=main_account.mid, uid=insta_user['id'],
                                             user_name=insta_user['username'],
                                             full_name=insta_user['full_name'], bio=insta_user['bio'],
                                             website=insta_user['website'],
                                             profile_picture=insta_user['profile_picture'],
                                             access_token=access_token)
            if insta_account_has_existed is not None:
                session.merge(insta_account)
            else:
                session.add(insta_account)
            session.commit()
            return Util.create_response(data=content)
        except Exception, e:
            print "OAuth Error %s" % (e.args[0])
            return Util.create_response(code=512, error='Save to db error:' + e.args[0])
