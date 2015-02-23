from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()


class Asset(Base):
    __tablename__ = 'asset'
    __table_args__ = {
        'mysql_charset': 'utf8' #utf8mb4
    }

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    mid = Column(INTEGER, index=True)
    type = Column(NVARCHAR(25))
    amount = Column(DECIMAL(10, 2))
    expire_time = Column(INTEGER)
    date_time = Column(INTEGER)


