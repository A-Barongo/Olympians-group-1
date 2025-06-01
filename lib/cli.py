from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from seed import engine


DATABASE_URL = "sqlite:///db/migrations/olympians.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
from helpers import(
    exit_program,
    get_all_appointments,
    find_appointment_by_patient_id,
    find_appointment_by_doctor_id,
    get_todays_appointments,
    find_appointments_by_date,
    update_appointment,
    create_appointment,
    delete_appointment_by_id,
    get_all_patients,
    find_patient_by_id,
    find_patient_by_name,
    find_patients_registered_today,
    create_patient,
    delete_patient_by_id,
    get_all_doctors,
    find_doctor_by_id,
    find_doctor_by_name,
    find_doctor_by_specialty,
    create_doctor,
    delete_doctor_by_id,
    update_doctor,
   

    

    
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_patient(session)
        elif choice == "2":
           get_all_patients(session)
        elif choice == "3":
            find_patient_by_id(session)
        elif choice == "4":
            find_patient_by_name(session)
        elif choice == "5":
           find_patients_registered_today(session)
        elif choice == "6":
           delete_patient_by_id(session)
        elif choice == "7":
            create_doctor(session)
        elif choice == "8":
           get_all_doctors(session)
        elif choice == "9":
           find_doctor_by_id(session)
        elif choice == "10":
           find_doctor_by_name(session)
        elif choice == "11":
           find_doctor_by_specialty(session)
        elif choice == "12":
            update_doctor(session)
        elif choice == "13":
            delete_doctor_by_id(session)
        elif choice == "14":
            create_appointment(session)
        elif choice == "15":
            delete_doctor_by_id(session)
        elif choice == "16":
             get_all_appointments(session)
        elif choice == "17":
          find_appointment_by_patient_id(session)
        elif choice == "18":
          find_appointment_by_doctor_id(session)
        elif choice == "19":
          get_todays_appointments(session)
        elif choice == "20":
         find_appointments_by_date(session)
        elif choice == "21":
          update_appointment(session)
        elif choice == "22":
         delete_appointment_by_id(session)
        else:
            print("Invalid choice")
            
def menu():
    print("")
    print("0. Exit the program")
    print("1. Create a new Patient")
    print("2. Get all Patients")
    print("3. Find Patient by ID")
    print("4. Find Patient by Name")
    print("5. Find Patients registered today")
    print("6. Delete Patient by ID")    
    print("2.  Create a new Doctor")
    print("8. Get all Doctors")
    print("9. Find Doctor by ID")
    print("10. Find Doctor by Name")
    print("11. Find Doctors by Specialty")
    print("12. Update Doctor")
    print("13. Delete Doctor by ID")
    print("14. Create a new Appointment")
    print("15. Delete Appointment by ID")
    print("16. Get all Appointments")
    print("17. Find Appointment by Patient ID")
    print("18. Find Appointment by Doctor ID")
    print("19. Get Today's Appointments")
    print("20. Find Appointments by Date")
    print("21. Update Appointment")
    print("22. Delete Appointment by ID")
   
    
if __name__ == "__main__":
    print("Welcome to the Olympians Hopital database.Select the functionality you require")
    main()
