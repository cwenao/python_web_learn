from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging; logging.basicConfig(level=logging.INFO)

ENGINE = create_engine("mysql+pymysql://root:123456@172.16.223.10:3306/pythontest?charset=utf8", max_overflow=5)

Session = sessionmaker(bind=ENGINE)
session = Session()


Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(INTEGER, primary_key=True)
    name = Column(String(32))
    passwd = Column(String(128))
    age = Column(INTEGER)
    status = Column(INTEGER)

    def __repr__(self):
        return "<UserInfo(name='%s')>" % self.name


def insert():
    user_info = UserInfo(id=1,name='a啊啊啊啊',status=1)
    session.add(user_info)
    session.commit()

insert()