"""Patient registration and lookup."""

import data
from validation import validate_patient


def add_patient(name, age_text, phone):
    error = validate_patient(name, age_text, phone)
    if error:
        return "Patient not added: " + error

    patient_id = "P" + str(data.NEXT_PATIENT_NUMBER).zfill(3)
    data.NEXT_PATIENT_NUMBER += 1

    patient = {
        "id": patient_id,
        "name": name,
        "age": int(age_text),
        "phone": phone
    }
    data.PATIENTS.append(patient)

    return (
        "Patient added successfully.\n"
        "Patient ID: " + patient["id"] + "\n"
        "Name: " + patient["name"] + "\n"
        "Age: " + str(patient["age"]) + "\n"
        "Phone: " + patient["phone"]
    )


def find_patient(patient_id):
    for patient in data.PATIENTS:
        if patient["id"] == patient_id:
            return patient
    return None


def list_patients():
    if not data.PATIENTS:
        print("No patients have been registered.")
        return

    print("\n--- Patient List ---")
    for patient in data.PATIENTS:
        print("Patient ID: " + str(patient["id"]))
        print("Name:       " + str(patient["name"]))
        print("Age:        " + str(patient["age"]))

        if "gender" in patient:
            print("Gender:     " + str(patient["gender"]))

        if "phone" in patient:
            print("Phone:      " + str(patient["phone"]))
        elif "contact" in patient:
            print("Contact:    " + str(patient["contact"]))
        else:
            print("Phone:      Not provided")

        print("--------------------")