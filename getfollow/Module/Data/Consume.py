# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class Consume(Base):
    __tablename__ = 'consume'
    __table_args__ = {
        'mysql_charset': 'utf8'  # utf8mb4
    }
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    consume_type = Column(VARCHAR(25))
    amount = Column(DECIMAL(10, 2))
    amount_left = Column(DECIMAL(10, 2))
    create_time = Column(BIGINT)
