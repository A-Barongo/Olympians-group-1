from db.models.appointment import Appointment,App_statusEnum, App_typeEnum
from db.models.patients import Patient, GenderEnum, StatusEnum
from datetime import datetime
def exit_program():
    print("Goodbye!")
    exit()
    
def get_all_appointments(session):
    appointments=Appointment.get_all_appointments(session)
    for appointment in appointments:
        print(appointment)
        
def find_appointment_by_patient_id(session):
    patient_id = input("Enter patient ID: ")
    appointments = Appointment.find_by_patient_id(session, patient_id)
    if appointments:
        for appointment in appointments:
            print(appointment)
    else:
        print(f"Patient ID {patient_id} not found")

def find_appointment_by_doctor_id(session):
    doctor_id = input("Enter doctor ID: ")
    appointments = Appointment.find_by_doctor_id(session, doctor_id)
    if appointments:
        for appointment in appointments:
            print(appointment)
    else:
        print(f"Doctor ID {doctor_id} not found")

def find_appointment_by_time(session):
    time = input('Enter appointment start time (HH:MM:SS): ')
    appointments = Appointment.find_by_time(session, time)
    if appointments:
        for appointment in appointments:
            print(appointment)
    else:
        print(f"No appointments start at {time}")
def update_appointment(session):
    appointment_id = input("Enter appointment ID:")
    appointment = Appointment.find_by_id(session, appointment_id)
    if appointment:
        try:
            date = input("Enter the new appointment date (YYYY-MM-DD): ")
            start_time = input("Enter the appointment's new start time (HH:MM:SS): ")
            end_time = input("Enter appointment's new end time: ")

            updated = Appointment.update_appointment(
                session,
                appointment_id,
                date=date,
                start_time=start_time,
                end_time=end_time
            )
            print(f'Success updating appointment id {appointment_id}to: {updated}')
        except Exception as exc:
            print("Error updating appointment: ", exc)
    else:
        print(f'Appointment ID {appointment_id} not found')

        
def create_appointment(session):
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    start_time = input("Enter appointment start time (HH:MM:SS): ")
    end_time = input("Enter appointment end time (HH:MM:SS): ")
    
    app_status_str = input(f"Enter appointment status {list(App_statusEnum.__members__.keys())}: ").lower()
    app_type_str = input(f"Enter appointment type {list(App_typeEnum.__members__.keys())}: ").lower()
    symptoms = input("Enter patient symptoms: ")
    notes = input("Enter any necessary notes about the patient: ")

    try:
        app_status_enum = App_statusEnum(app_status_str.replace(' ', '_'))
        app_type_enum = App_typeEnum(app_type_str.replace(' ', '_'))

        Appointment.create_appointment(
            session,
            patient_id, doctor_id, date, start_time, end_time,
            app_status_enum, app_type_enum, notes, symptoms
        )
        print("Appointment created successfully.")
    except Exception as exc:
        print("Error creating appointment:", exc)
     
def delete_appointment_by_id(session):
    appointment_id = input("Enter the appointment ID: ")
    success = Appointment.delete_by_id(session, appointment_id)
    if success:
        print("Appointment deleted.")
    else:
        print("Appointment not found.")
        
#Patients helper code

def get_all_patients(session):
    patients = Patient.get_all_patients(session)
    if patients:
        for patient in patients:
            print(patient)
    else:
        print("No patients found.")

def find_patient_by_id(session):
    patient_id = input("Enter patient ID: ")
    patient = Patient.get_by_id(session, int(patient_id))
    if patient:
        print(patient)
    else:
        print(f"No patient found with ID {patient_id}.")

def find_patient_by_name(session):
    name = input("Enter patient name: ")
    results = Patient.find_by_name(session, name)
    if results:
        for patient in results:
            print(patient)
    else:
        print(f"No patients found with name '{name}'.")

def find_patients_registered_today(session):
    patients = Patient.get_all_today(session)
    if patients:
        print("Patients registered today:")
        for p in patients:
            print(p)
    else:
        print("No patients registered today.")

def create_patient(session):
    try:
        name = input("Enter name: ")
        dob_input = input("Enter date of birth (YYYY-MM-DD): ")
        date_of_birth = datetime.strptime(dob_input, "%Y-%m-%d").date()

        gender_input = input(f"Enter gender {list(GenderEnum.__members__.keys())}: ").lower()
        gender_enum = GenderEnum[gender_input]

        email = input("Enter email: ")

        status_input = input(f"Enter status {list(StatusEnum.__members__.keys())}: ").lower()
        status_enum = StatusEnum[status_input]

        current_medication = input("Enter current medication (optional): ")
        chronic_conditions = input("Enter chronic conditions (optional): ")

        new_patient = Patient.create_patient(
            session,
            name=name,
            date_of_birth=date_of_birth,
            gender=gender_enum,
            email=email,
            status=status_enum,
            current_medication=current_medication,
            chronic_conditions=chronic_conditions
        )
        print("Patient created:", new_patient)
    except Exception as e:
        print("Error creating patient:", e)

def delete_patient_by_id(session):
    patient_id = input("Enter patient ID to delete: ")
    success = Patient.delete_by_id(session, int(patient_id))
    if success:
        print("Patient deleted.")
    else:
        print("Patient not found.")


