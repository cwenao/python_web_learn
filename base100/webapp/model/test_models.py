from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String
from base100.crawler import db_operation


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
    user_info = UserInfo(id=2,name='你好',status=1)
    session = db_operation.get_session()
    session.add(user_info)
    session.commit()


insert()