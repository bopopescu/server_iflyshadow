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
    user_name = Column(NVARCHAR(25))
    full_name = Column(NVARCHAR(25))
    user_password = Column(VARCHAR(25))