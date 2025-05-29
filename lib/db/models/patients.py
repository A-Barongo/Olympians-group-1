from sqlalchemy import Column, Integer, String, DateTime, Enum, func, Date
from sqlalchemy.orm import Session

import enum
from datetime import date


from .base import Base

# Enum classes
class StatusEnum(enum.Enum):
    inpatient = "inpatient"
    outpatient = "outpatient"
    discharged = "discharged"

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    other = "other"


# Patient model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False) 
    gender = Column(Enum(GenderEnum), nullable=False)
    email = Column(String, nullable=False, unique=True)
    status = Column(Enum(StatusEnum),nullable=False)
    current_medication = Column(String)
    chronic_conditions = Column(String)
    date_registered = Column(DateTime, server_default=func.now())

def __repr__(self):
    return(
        f"<Patient(id={self.id}, name={self.name}, email={self.email})>"
        f"<Status=`{self.status.name}`, registered={self.date_registered}>"
        )

# Properties

@property
def age(self):
    today = date.today()
    return today.year - self.date_of_birth.year - (
        (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

def is_adult(self):
    return self.age >= 18 

# Class methods for CRUD operations 
@classmethod
def get_all_patients(cls, session: Session):
    return session.query(cls).all()


@classmethod
def get_all_today(cls, session: Session):
    today = date.today()
    return session.query(cls).filter(
        func.date(cls.date_registered) == today 
        ).all()


@classmethod
def find_by_name(cls, session: Session, name: str):
    return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()


@classmethod
def delete_by_id(cls, session: Session, patient_id: int):
    patient = session.query(cls).get(patient_id)
    if patient:
        session.delete(patient)
        session.commit()
        return True
    return False

# Class method to create a new patient
@classmethod
def create_patient(cls, session: Session, name: str, date_of_birth: date, gender: GenderEnum, email: str, status: StatusEnum, current_medication: str, chronic_conditions: str):
    new_patient = cls(
        name=name,
        date_of_birth=date_of_birth,
        gender=gender,
        email=email,
        status=status,
        current_medication=current_medication,
        chronic_conditions=chronic_conditions
        )
    session.add(new_patient)
    session.commit()
    return new_patient
