
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
# Make sure Appointment is imported if used in relationships
from .appointment import Appointment  # Uncomment and adjust if needed

class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, )
    contact_info= Column(String,)
    national_id = Column(String, unique=True, nullable=False)
    medical_license_number = Column(String, unique=True, nullable=False)
    
    appointments = relationship("Appointment", back_populates="doctor" ,cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"<Doctor(id={self.id}, name='{self.name}', specialty='{self.specialty}', "
            f"national_id='{self.national_id}', license_no='{self.medical_license_number}')>"
        )
    @classmethod
    def create_doctor(cls, session, name: str, specialty: str, contact_info: str, national_id: str, medical_license_number: str):
        
        new_doctor = cls(
            name=name,
            specialty=specialty,
            contact_info=contact_info,
            national_id=national_id,
            medical_license_number=medical_license_number
        )
        session.add(new_doctor)
        session.commit()
        return new_doctor
    @classmethod
    def get_by_id(cls, session, doctor_id:int):
        return session.query(cls).filter_by(id=doctor_id).first()
    
    @classmethod
    def get_all_doctors(cls, session):
        
        return session.query(cls).all()
    
    @classmethod
    def delete_by_id(cls, session, doctor_id:int):
        doctor = session.query(cls).filter_by(id=doctor_id).first()
        if doctor:
            session.delete(doctor)
            session.commit()
            return True
        return False
         
   

    @classmethod
    def find_by_name(cls, session, name:str):
        
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @classmethod
    def find_by_specialty(cls, session, specialty):
        return session.query(cls).filter(cls.specialty.ilike(f"%{specialty}%")).all()
    
    @classmethod
    def find_by_time(cls, session, time_str):
        # List of tuples: (Doctor Name, Time)
        return [
            (doc.name, appt.time)
            for doc in session.query(cls).join(cls.appointments).all()
            for appt in doc.appointments
            if appt.start_time == time_str
        ]
        
    @classmethod
    def find_by_patient(cls, session, patient_name):
        # List of dicts: each doctor with patient they treated
        return (
            session.query(cls)
            .join(Appointment)
            .join(Appointment.patient) # Direct join through relationship
            .filter(Appointment.patient.has(name=patient_name)) # Use has() for relationship filtering
            .distinct() # To get unique doctors
            .all()
        )
       
