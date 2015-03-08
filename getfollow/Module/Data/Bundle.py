# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.dialects.mysql import *

Base = declarative_base()


class Bundle(Base):
    __tablename__ = 'application'
    __table_args__ = {
        'mysql_charset': 'utf8'  # utf8mb4
    }

    id = Column(VARCHAR(25), autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    uid = Column(INTEGER, index=True)

    session_id = Column(VARCHAR(25))
    # 65位:86969fbcd6f0914166e3fded2f3fb38c5215e9547ccc6cef3199d3b42cbac8bf
    device_token = Column(VARCHAR(100))

    # com.ideastray.GetFollow
    bundle_id = Column(VARCHAR(100))
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



