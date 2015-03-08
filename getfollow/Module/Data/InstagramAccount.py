# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.dialects.mysql import *

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



