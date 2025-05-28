from helpers import(
    exit_program,
    get_all_appointments,
    find_appoinment_by_patient_id,
    find_appointment_by_doctor_id,
    find_appointement_by_time,
    get_patient_status_by_id,
    get_appointment_description_by_patient_id,
    delete_appointment_by_patient_id,
    delete_appointment_by_doctor_id
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_appointments()
        elif choice == "2":
            pass
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
    print("1. ")
    print("2. ")
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
    main()
