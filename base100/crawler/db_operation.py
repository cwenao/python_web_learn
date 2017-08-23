from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging; logging.basicConfig(level=logging.INFO)


ENGINE = create_engine("mysql+pymysql://root:123456@172.16.223.10:3306/pythontest?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=ENGINE)
global session


def get_session():
    global session
    session = Session()
    return session


def get_engine():
    return ENGINE


