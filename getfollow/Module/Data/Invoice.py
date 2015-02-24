# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class Invoice(Base):
    __tablename__ = 'invoice'
    __table_args__ = {
        'mysql_charset': 'utf8' #utf8mb4
    }
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    invoice_type = Column(VARCHAR(25))
    amount = Column(DECIMAL(10, 2))
    date_time = Column(BIGINT, index=True)
