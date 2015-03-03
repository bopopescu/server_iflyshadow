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
    session_id = Column(VARCHAR(25))

    user_name = Column(NVARCHAR(25))
    full_name = Column(NVARCHAR(25))
    bio = Column(NVARCHAR(50))
    website = Column(VARCHAR(50))
    profile_picture = Column(VARCHAR(100))
    media = Column(INTEGER)
    followed_by = Column(INTEGER)
    follows = Column(INTEGER)

    igm_user = Column(VARCHAR(25))
    igm_password = Column(VARCHAR(25))
    # 50位:37004920.aa175a6.ab9dfbf920774ff9baa1413cf14ca91f
    access_token = Column(VARCHAR(70))

    latitude = Column(DOUBLE(12, 8), index=True)
    longitude = Column(DOUBLE(12, 8), index=True)

    # 65位:86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf
    device_token = Column(VARCHAR(100))
    # iPhone OS 8.1.3
    device_system_name = Column(VARCHAR(25))
    # iPhone 6
    device_platform = Column(VARCHAR(25))
    # iPhone OS 8.1.3
    device_system_name = Column(VARCHAR(25))
    # com.ideastray.GetFollow
    bundle_identifier = Column(VARCHAR(50))
    # iPhone OS 8.1.3
    bundle_version = Column(VARCHAR(25))
    # iPhone OS 8.1.3
    device_system_name = Column(VARCHAR(25))




