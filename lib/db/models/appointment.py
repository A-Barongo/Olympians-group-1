from .base import Base
import enum 
from sqlalchemy import ForeignKey, Table, Column, Integer, String, Date,Time,Enum
from sqlalchemy.orm import relationship, Session
from typing import Union
from datetime import datetime
from datetime import date
from sqlalchemy import func
#from .patient import Patient


class App_statusEnum(enum.Enum):
   scheduled='scheduled' 
   checked_in='checked in' 
   cancelled='cancelled'
   completed='completed' 
   no_show='no show'
class App_typeEnum(enum.Enum):
    consultation="consultation"
    follow_up="follow up" 
    surgery="surgery"
    emergency="emergency"
    
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    patient_id=Column(Integer,ForeignKey('patients.id'), nullable=False)
    doctor_id=Column(Integer,ForeignKey('doctors.id'), nullable=False)
    date=Column(Date, nullable=False)
    start_time=Column(Time, nullable=False)
    end_time=Column(Time())
    app_status = Column(Enum(App_statusEnum),nullable=False)
    app_type= Column(Enum(App_typeEnum),nullable=False)
    notes=Column(String())
    symptoms=Column(String())
    
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
    
    def __repr__(self):
        return f"Appointment(id={self.id}, date={self.date}, start time={self.start_time}, end time={self.end_time}, doctor_id={self.doctor_id}, patient_id={self.patient_id})"

    
    @classmethod
    def create_appointment(
    cls,session: Session,patient_id: int,doctor_id: int, date: Date, start_time: Time, end_time: Time,
    app_status: App_statusEnum,app_type:App_typeEnum, notes:str ,symptoms:str):
       
        new_appointment=cls(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            start_time=start_time,
            end_time=end_time,
            app_status=app_status,
            app_type=app_type,
            notes=notes,
            symptoms=symptoms
        )
        session.add(new_appointment)
        session.commit()
        return new_appointment
    
    @classmethod
    def get_all_appointments(cls, session: Session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls,session: Session,app_id):
        return session.query(cls).filter_by(id=app_id).first()
    
    @classmethod
    def delete_by_id(cls, session: Session, app_id: int) -> bool:
        appointment = session.query(cls).filter_by(id=app_id).first()
        if appointment:
            session.delete(appointment)
            session.commit()
            return True
        return False
    @classmethod
    def get_by_date(cls, session: Session, target_date: Date):
        return session.query(cls).filter(cls.date == target_date).all()
    
    @classmethod
    def find_by_patient_id(cls,session: Session,patient_id:int):
        return session.query(cls).filter_by(patient_id=patient_id).all()
    
    @classmethod
    def find_by_doctor_id(cls,session: Session,doctor_id:int):
        return session.query(cls).filter_by(doctor_id=doctor_id).all()
    
    @classmethod
    def find_by_status(cls, session: Session, status: App_statusEnum):
       
        return session.query(cls).filter_by(app_status=status).all()
    
      

    @classmethod
    def update_appointment(cls, session: Session, appointment_id: int, **kwargs) -> Union["Appointment", None]: # <--- MODIFIED THIS LINE
        
        appointment = cls.find_by_id(session, appointment_id)
        if not appointment:
            return None

        for key, value in kwargs.items():
            if hasattr(appointment, key):
                setattr(appointment, key, value)
        
        session.commit()
        return appointment
    
    
    @classmethod
    def get_appointments_today(cls, session: Session):
        today = date.today()
        return session.query(cls).filter(func.date(cls.date) == today).all()   