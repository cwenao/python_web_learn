from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


BaseModel = declarative_base()


class ProviderInfo(BaseModel):
    __tablename__ = 'provider_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    provider_name = Column(String(128))
    status = Column(Integer)