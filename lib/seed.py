from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date, time

from db.models.appointment import Appointment, App_statusEnum, App_typeEnum
from db.models.base import Base
from db.models.patients import Patient
from db.models.doctor import Doctor


DATABASE_URL = "sqlite:///db/migrations/olympians.db"  

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def seed_appointments():
    sample_appointments = [
        {
            "patient_id": 1,
            "doctor_id": 1,
            "date": date(2025, 6, 1),
            "start_time": time(9, 0),
            "end_time": time(9, 30),
            "app_status": App_statusEnum.scheduled,
            "app_type": App_typeEnum.consultation,
            "notes": "First time consultation.",
            "symptoms": "Headache, fatigue"
        },
        {
            "patient_id": 2,
            "doctor_id": 2,
            "date": date(2025, 6, 2),
            "start_time": time(10, 0),
            "end_time": time(10, 45),
            "app_status": App_statusEnum.completed,
            "app_type": App_typeEnum.follow_up,
            "notes": "Follow-up after surgery.",
            "symptoms": "Mild pain"
        },
        {
            "patient_id": 3,
            "doctor_id": 1,
            "date": date(2025, 6, 3),
            "start_time": time(11, 0),
            "end_time": time(11, 30),
            "app_status": App_statusEnum.cancelled,
            "app_type": App_typeEnum.emergency,
            "notes": "Patient cancelled last minute.",
            "symptoms": "N/A"
        },
    ]

    for appt_data in sample_appointments:
        appointment = Appointment.create_appointment(session, **appt_data)
        print(f"Created appointment ID: {appointment.id}")

if __name__ == "__main__":
    # Create tables if they don’t exist
    Base.metadata.create_all(engine)

    # Run seeding
    seed_appointments()
