from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
import config

Base = declarative_base()
engine = create_engine(config.DATABASE_URL, echo=False)


class Refugee(Base):
    __tablename__ = "Refugees"
    refugee_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    primary_language = Column(String)
    secondary_language = Column(String)
    family_size = Column(Integer)
    previous_occupation = Column(String)
    profile_picture = Column(String)


class HostFamily(Base):
    __tablename__ = "Host_Families"
    host_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    primary_language = Column(String)
    secondary_language = Column(String)
    family_size = Column(Integer)
    available_space = Column(Integer)
    occupation = Column(String)
    salary = Column(Integer)
    location = Column(String)
    profile_picture = Column(String)
    preffered_size = Column(Integer)
