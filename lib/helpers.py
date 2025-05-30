from db.models.appointment import Appointment,App_statusEnum, App_typeEnum

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


