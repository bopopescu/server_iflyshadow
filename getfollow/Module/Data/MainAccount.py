# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class MainAccount(Base):
    __tablename__ = 'main_account'
    __table_args__ = {
        'mysql_charset': 'utf8'  # utf8mb4
    }
    mid = Column(INTEGER, autoincrement=True, primary_key=True)
    last_access_time = Column(BIGINT)
    device_token = Column(VARCHAR(255))
    device = Column(VARCHAR(15))
    device_os = Column(VARCHAR(25))
    ip_address = Column(VARCHAR(20))