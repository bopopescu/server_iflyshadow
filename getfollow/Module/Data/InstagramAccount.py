# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker

from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.Bundle import *
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

    def save(self, access_token, insta_user_json):
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

        try:
            # 4.1 merge MainAccount or add
            My_Session = sessionmaker(bind=MYSQL_ENGINE)
            my_session = My_Session()
            main_account = MainAccount(user_name=insta_user_json['username'],
                                       full_name=insta_user_json['full_name'])
            insta_account_has_existed = my_session.query(InstagramAccount).filter(
                InstagramAccount.uid == insta_user_json['id']).first()
            if insta_account_has_existed is not None:
                main_account.mid = insta_account_has_existed.mid
                my_session.merge(main_account)
            else:
                my_session.add(main_account)
            my_session.commit()

            # 4.1 merge MainAccount or add
            insta_account = InstagramAccount(mid=main_account.mid, uid=insta_user_json['id'],
                                             user_name=insta_user_json['username'],
                                             full_name=insta_user_json['full_name'], bio=insta_user_json['bio'],
                                             website=insta_user_json['website'],
                                             profile_picture=insta_user_json['profile_picture'],
                                             access_token=access_token)
            if 'counts' in insta_user_json:
                counts_json = insta_user_json['counts']
                if 'media' in counts_json:
                    self.media = counts_json['media']
                if 'follows' in counts_json:
                    self.follows = counts_json['follows']
                if 'followed_by' in counts_json:
                    self.followed_by = counts_json['followed_by']

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


