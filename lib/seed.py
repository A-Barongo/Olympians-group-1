from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date, time
from faker import Faker
import random

from db.models.appointment import Appointment, App_statusEnum, App_typeEnum
from db.models.base import Base
from db.models.patients import Patient, GenderEnum, StatusEnum
from db.models.doctor import Doctor

DATABASE_URL = "sqlite:///db/migrations/olympians.db"  

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def clear_data():
    session.query(Appointment).delete()
    session.query(Patient).delete()
    session.query(Doctor).delete()
    session.commit()

def seed_doctors():
    specialties = [
        'Cardiology', 'Pediatrics', 'Neurology', 'Oncology', 'Orthopedics',
        'General Surgery', 'Dermatology', 'Radiology', 'Psychiatry', 'Family Medicine'
    ]
    for i in range(10):
        try:
            doc = Doctor.create_doctor(
                session,
                name=f"Dr. {fake.name()}",
                specialty=specialties[i % len(specialties)],
                contact_info=fake.email(),
                national_id=f"ID{fake.unique.random_number(digits=6)}",
                medical_license_number=f"LIC{fake.unique.random_number(digits=4)}"
            )
            print(f"Seeded doctor: {doc.name}")
        except Exception as e:
            print(f"Error seeding doctor: {e}")

def seed_patients():
    for _ in range(20):
        gender_choice = random.choice(['male', 'female'])
        try:
            patient = Patient.create_patient(
                session,
                name=fake.name_male() if gender_choice == 'male' else fake.name_female(),
                date_of_birth=fake.date_of_birth(minimum_age=10, maximum_age=90),
                gender=GenderEnum[gender_choice],
                email=fake.unique.email(),
                status=StatusEnum[random.choice(['inpatient', 'outpatient', 'discharged'])],
                current_medication=fake.word(),
                chronic_conditions=fake.word()
            )
            print(f"Seeded patient: {patient.name}")
        except Exception as e:
            print(f"Failed to seed patient: {e}")

def seed_appointments():
    for _ in range(30):
        try:
            start_hour = random.randint(8, 16)
            start = time(start_hour, 0)
            end = time(start_hour, 30)

            appointment = Appointment.create_appointment(
                session,
                patient_id=random.randint(1, 20),
                doctor_id=random.randint(1, 10),
                date=fake.date_between(start_date="today", end_date="+30d"),
                start_time=start,
                end_time=end,
                app_status=App_statusEnum[random.choice(['scheduled', 'completed', 'cancelled'])],
                app_type=App_typeEnum[random.choice(['consultation', 'follow_up', 'emergency'])],
                notes=fake.sentence(),
                symptoms=fake.sentence()
            )
            print(f"Created appointment ID: {appointment.id}")
        except Exception as e:
            print(f"Failed to seed appointment: {e}")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    clear_data()
    seed_doctors()
    seed_patients()
    seed_appointments()
