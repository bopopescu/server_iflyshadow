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

    uid = Column(VARCHAR(25), autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    user_name = Column(NVARCHAR(25))
    full_name = Column(NVARCHAR(25))
    bio = Column(NVARCHAR(100))
    website = Column(VARCHAR(100))
    profile_picture = Column(VARCHAR(100))
    media = Column(INTEGER)
    followed_by = Column(INTEGER)
    follows = Column(INTEGER)
    latitude = Column(DOUBLE(10, 6))
    longitude = Column(DOUBLE(10, 6))
    access_token = Column(VARCHAR(50))

