# -*- coding: utf-8 -*-


import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import sessionmaker
from getfollow.Module.Utils.Util import *


Base = declarative_base()


class BundleUser(Base):
    __tablename__ = 'bundle_user'
    __table_args__ = {
        'mysql_charset': 'utf8'  # utf8mb4
    }

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    uid = Column(INTEGER, index=True)
    # 101:com.ideastray.GetFollow
    bundle_id = Column(INTEGER, index=True)

    session_id = Column(VARCHAR(50), index=True)
    # 65位:86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf
    device_token = Column(VARCHAR(100))
    # 1
    bundle_version = Column(INTEGER)

    # en_US
    locale_identifier = Column(VARCHAR(15))
    # en/zh-Hans
    preferred_language = Column(VARCHAR(15))

    # iPhone OS
    device_os_name = Column(VARCHAR(15))
    # 8.1
    device_os_version = Column(VARCHAR(15))
    # iPhone 6
    device_model = Column(VARCHAR(25))

    latitude = Column(DOUBLE(12, 8), index=True)
    longitude = Column(DOUBLE(12, 8), index=True)

    last_ip_address = Column(VARCHAR(20))
    last_access_time = Column(BIGINT)
    create_time = Column(BIGINT)

    def update_to_db(self, mid, uid, bundle_info_json, is_login=False):
        try:
            if 'bundle_id' not in bundle_info_json:
                return False, 400, 'no bundle_id'
            self.bundle_id = bundle_info_json['bundle_id']
            if self.bundle_id is None:
                return False, 400, 'no bundle_id'
            if mid is None:
                return False, 400, 'no mid'
            self.mid = mid
            if uid is None:
                return False, 400, 'no uid'
            self.uid = uid
            if 'session_id' in bundle_info_json:
                self.session_id = bundle_info_json['session_id']
            if 'device_token' in bundle_info_json:
                self.device_token = bundle_info_json['device_token']
            if 'bundle_version' in bundle_info_json:
                self.bundle_version = bundle_info_json['bundle_version']
            if 'locale_identifier' in bundle_info_json:
                self.locale_identifier = bundle_info_json['locale_identifier']
            if 'preferred_language' in bundle_info_json:
                self.preferred_language = bundle_info_json['preferred_language']
            if 'device_os_name' in bundle_info_json:
                self.device_os_name = bundle_info_json['device_os_name']
            if 'device_os_version' in bundle_info_json:
                self.device_os_version = bundle_info_json['device_os_version']
            if 'device_model' in bundle_info_json:
                self.device_model = bundle_info_json['device_model']
            if 'latitude' in bundle_info_json:
                self.latitude = bundle_info_json['latitude']
            if 'longitude' in bundle_info_json:
                self.longitude = bundle_info_json['longitude']

            self.last_access_time = int(time.time() * 1000)
            self.last_ip_address = request.headers.get('X-Real-Ip', request.remote_addr)

            My_Session = sessionmaker(bind=MYSQL_ENGINE)
            my_session = My_Session()

            bundle_user_has_existed = my_session.query(BundleUser).filter(
                BundleUser.uid == self.uid and BundleUser.mid == self.mid and BundleUser.uid == self.uid and BundleUser.bundle_id == self.bundle_id).first()
            if bundle_user_has_existed is not None:
                if is_login:
                    # login
                    self.session_id = Util.get_session_id()
                elif bundle_user_has_existed.session_id != self.session_id:
                    # not login but session id is invalid
                    return False, Util.CODE_SESSION_ID_IS_INVALID, 'session id is invalid!'
                # merge
                self.id = bundle_user_has_existed.id
                self.create_time = bundle_user_has_existed.create_time
                my_session.merge(self)
            else:
                if is_login:
                    # first login
                    self.session_id = Util.get_session_id()
                    self.create_time = int(time.time() * 1000)
                    my_session.add(self)
                else:
                    # not login but session id is invalid
                    return False, Util.CODE_SESSION_ID_IS_INVALID, 'session id is invalid!'
            # commit
            my_session.commit()
            return True, 200, ''
        except Exception, e:
            err_info = "Bundle user update Error %s" % (e.args[0])
            print(err_info)
            return False, 513, err_info