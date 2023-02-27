import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Enum, DateTime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from ybvdl.db import Base
from ybvdl.client_types import SexEnum, MaritalStatusEnum


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    vk_id = Column(String, nullable=False)

    name = Column(String, nullable=False)
    about_info = Column(String, nullable=True)

    gender = Column(Enum(SexEnum), nullable=False, default=SexEnum.UNDEFINED)
    marital_status = Column(Enum(MaritalStatusEnum), nullable=True)

    last_updated = Column(DateTime, nullable=False, onupdate=datetime.datetime.now)
    created = Column(DateTime, nullable=False, default=datetime.datetime.now)
