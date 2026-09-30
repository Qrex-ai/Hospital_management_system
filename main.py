"""Hospital Management System."""

from patients import add_patient, find_patient, list_patients
from doctors import list_doctors
from appointments import book_appointment, list_appointments
from billing import create_bill, list_bills
from reports import show_summary


def show_menu():
    print("\n=== COMMUNITY CLINIC RECORD SYSTEM ===")
    print("1. Register patient")
    print("2. View patients")
    print("3. Search patient")
    print("4. View doctors")
    print("5. Book appointment")
    print("6. View appointments")
    print("7. Create bill")
    print("8. View bills")
    print("9. Summary report")
    print("0. Exit")


def run_app():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Patient name: ").strip()
            age = int(input("Age in years: ").strip())
            phone = input("Phone (digits only): ").strip()
            result = add_patient(name, age, phone)
            print(result)
        elif choice == "2":
            list_patients()
        elif choice == "3":
            patient_id = ("Patient ID: ").strip().upper()
            patient = find_patient(patient_id)

            if patient is None:
                print("No patient found with that ID.")
            else:
                print("\n--- Patient Details ---")
                print("Patient ID: " + str(patient["id"]))
                print("Name:       " + str(patient["name"]))
                print("Age:        " + str(patient["age"]))

                if "gender" in patient:
                    print("Gender:     " + str(patient["gender"]))

                if "phone" in patient:
                    print("Phone:      " + str(patient["phone"]))
                elif "contact" in patient:
                    print("Contact:    " + str(patient["contact"]))

                print("-----------------------")
        elif choice == "4":
            list_doctors()
        elif choice == "5":
            patient_id = input("Patient ID: ").strip().upper()
            doctor_id = input("Doctor ID: ").strip().upper()
            visit_date = input("Appointment date (YYYY-MM-DD): ").strip()
            visit_time = input("Appointment time (HH:MM AM/PM): ").strip()
            print(book_appointment(patient_id, doctor_id, visit_date, visit_time))
        elif choice == "6":
            list_appointments()
        elif choice == "7":
            patient_id = input("Patient ID: ").strip().upper()
            amount = float(input("Bill amount (whole rupees): ").strip())
            print(create_bill(patient_id, amount))
        elif choice == "8":
            list_bills()
        elif choice == "9":
            show_summary()
        elif choice == "0":
            print("Goodbye. Demo records will be cleared when this program closes.")
            break
        else:
            print("Please enter a number from 0 to 9.")


if __name__ == "__main__":
    run_app()
