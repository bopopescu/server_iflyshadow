# -*- coding: utf-8 -*-

import time

from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.BundleUser import *
from getfollow.Module.Utils.Util import *


Base = declarative_base()


class InstagramAccount(Base):
    __tablename__ = 'instagram_account'
    __table_args__ = {
        'mysql_charset': 'utf8'  # utf8mb4
    }

    uid = Column(VARCHAR(25), primary_key=True)
    mid = Column(INTEGER, index=True)

    igm_user = Column(VARCHAR(25))
    igm_password = Column(VARCHAR(25))

    user_name = Column(NVARCHAR(25))
    full_name = Column(NVARCHAR(25))
    bio = Column(NVARCHAR(50))
    website = Column(VARCHAR(50))
    profile_picture = Column(VARCHAR(100))
    media = Column(INTEGER)
    followed_by = Column(INTEGER)
    follows = Column(INTEGER)

    # 50位:37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f
    access_token = Column(VARCHAR(70))
    create_time = Column(BIGINT)

    def update_to_db(self, igm_user_json, access_token=None, igm_user=None, igm_password=None):
        My_Session = sessionmaker(bind=MYSQL_ENGINE)
        my_session = My_Session()
        try:
            # 1 merge MainAccount or add
            main_account = MainAccount(user_name=igm_user_json['username'],
                                       full_name=igm_user_json['full_name'])
            insta_account_has_existed = my_session.query(InstagramAccount).filter(
                InstagramAccount.uid == igm_user_json['id']).first()
            if insta_account_has_existed is not None:
                main_account.mid = insta_account_has_existed.mid

                my_session.merge(main_account)
            else:
                main_account.create_time = int(time.time() * 1000)
                my_session.add(main_account)
            my_session.commit()

            # 2 merge MainAccount or add
            self.mid = main_account.mid
            self.uid = igm_user_json['id']
            self.user_name = igm_user_json['username']
            self.full_name = igm_user_json['full_name']
            self.bio = igm_user_json['bio']
            self.website = igm_user_json['website']
            self.profile_picture = igm_user_json['profile_picture']

            if access_token is not None:
                self.access_token = access_token
            if igm_user is not None:
                self.igm_user = igm_user
            if igm_user is not None:
                self.igm_password = igm_password
            if 'counts' in igm_user_json:
                counts_json = igm_user_json['counts']
                if 'media' in counts_json:
                    self.media = counts_json['media']
                if 'follows' in counts_json:
                    self.follows = counts_json['follows']
                if 'followed_by' in counts_json:
                    self.followed_by = counts_json['followed_by']

            if insta_account_has_existed is not None:
                self.create_time = insta_account_has_existed.create_time
                my_session.merge(self)
            else:
                self.create_time = int(time.time() * 1000)
                my_session.add(self)
            my_session.commit()
            return True, 200, ''
        except Exception, e:
            err_info = "Instagram account update Error %s" % (e.args[0])
            print(err_info)
            return False, 512, err_info

            # "data": {
            # "id": "1574083",
            # "username": "snoopdogg",
            # "full_name": "Snoop Dogg",
            # "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
            # "bio": "This is my bio",
            # "website": "http://snoopdogg.com",
            # "counts": {
            # "media": 1320,
            # "follows": 420,
            # "followed_by": 3410
            # }
