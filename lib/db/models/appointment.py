from .base import Base
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime



class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)