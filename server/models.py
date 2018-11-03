from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Refugee(Base):
    __tablename__ = "Refugees"
    refugee_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    primary_language = Column(String)
    secondary_language = Column(String)
    family_size = Column(Integer)
    previous_occupation = Column(String)

class HostFamily(Base):
    __tablename__ = "Host Families"
    host_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    primary_language = Column(String)
    secondary_language = Column(String)
    available_space = Column(Integer)
    occupation = Column(String)
    salary = Column(String)
    location = Column(String)