# -*- coding: utf-8 -*-
__author__ = 'sharp'
import urllib
import time

from flask import request, jsonify, make_response
import simplejson
from httplib2 import Http
from getfollow.Config.Consts import *
from sqlalchemy.orm import sessionmaker
from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.InstagramAccount import *


class InstagramOAuth(object):
    get_access_token_url = None

    def __init__(self):
        self.get_access_token_url = GET_FOLLOW_CONFIG.ACCESS_TOKEN_REQUEST_URI

    def exchange_for_access_token(self, ):
        if request.method == 'GET':

            # 1. get code error
            error = request.args.get('error')
            if error is not None:
                error_reason = request.args.get('error_reason')
                error_description = request.args.get('error_description')
                return make_response(jsonify({'code': 511, 'error': error, 'error_reason': error_reason,
                                              'error_description': error_description}), 500)

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
                return make_response(jsonify(
                    {'code': int(response['status']), 'error': 'Exchange Access_token error', 'error_reason': '',
                     'error_description': parsed_content.get("error_message", "")}), 500)

            # 4. succeed
            Session = sessionmaker(bind=MYSQL_ENGINE)
            session = Session()

            access_token = parsed_content['access_token']
            insta_user = parsed_content['user']

            # 4.1 merge MainAccount or add
            main_account = MainAccount(last_access_time=time.time(), ip_address=request.remote_addr)
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
                                             profile_picture=insta_user['profile_picture'], access_token=access_token)
            if insta_account_has_existed is not None:
                session.merge(insta_account)
            else:
                session.add(insta_account)
            session.commit()
            return make_response(content, 200)