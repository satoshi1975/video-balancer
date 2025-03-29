from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True, index=True)
    cdn_host = Column(String, nullable=False)
    ratio = Column(Integer, nullable=False)
