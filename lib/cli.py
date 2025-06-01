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
    delete_patient_by_id
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_appointments(session)
        elif choice == "2":
            get_all_patients(session)
        elif choice == "3":
           pass 
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        elif choice == "13":
            pass
        else:
            print("Invalid choice")
            
def menu():
    print("")
    print("0. Exit the program")
    print("1. Get all appointments")
    print("2. Get all Patients")
    print("3. ")
    print("4: ")
    print("5: ")
    print("6: ")
    print("7. ")
    print("8. ")
    print("9. ")
    print("10: ")
    print("11: ")
    print("12: ")
    print("13: ")
    
if __name__ == "__main__":
    print("Welcome to the Olympians Hopital database.Select the functionality you require")
    main()
