from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.models import Base
# Make sure Appointment is imported if used in relationships
# from .appointment import Appointment  # Uncomment and adjust if needed

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
    def get_by_id(cls, session, doctor_id):
        doctor = session.query(cls).filter_by(id=doctor_id).first()
        if doctor:
            return {
                "id": doctor.id,
                "name": doctor.name,
                "specialty": doctor.specialty,
                "contact_info": doctor.contact_info,
            }
        return None
    
    @classmethod
    def delete_by_id(cls, session, doctor_id):
        doctor = session.query(cls).filter_by(id=doctor_id).first()
        if doctor:
            session.delete(doctor)
            session.commit()
            return True
        return False
         
   

    @classmethod
    def find_by_name(cls, session, name):
        doctors = session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
        # Return a list of tuples: (id, name, specialty)
        return [(doc.id, doc.name, doc.specialty) for doc in doctors]
    
    @classmethod
    def find_by_specialty(cls, session, specialty):
        doctors = session.query(cls).filter(cls.specialty.ilike(f"%{specialty}%")).all()

        return [{
            "id": doc.id,
            "name": doc.name,
            "specialty": doc.specialty,
            "contact_info": doc.contact_info
        } for doc in doctors

        ]
    
    @classmethod
    def find_by_time(cls, session, time_str):
        # List of tuples: (Doctor Name, Time)
        return [
            (doc.name, appt.time)
            for doc in session.query(cls).join(cls.appointments).all()
            for appt in doc.appointments
            if appt.time == time_str
        ]
        
    @classmethod
    def find_by_patient(cls, session, patient_name):
        # List of dicts: each doctor with patient they treated
        results = []
        for doc in session.query(cls).join(cls.appointments).join(Appointment.patient).all():
            for appt in doc.appointments:
                if appt.patient and patient_name.lower() in appt.patient.name.lower():
                    results.append({
                        "doctor_name": doc.name,
                        "patient_name": appt.patient.name,
                        "appointment_time": appt.time
                    })
        return results
       