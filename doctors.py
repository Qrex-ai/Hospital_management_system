"""Doctor directory."""

import data


def list_doctors():
    if not data.DOCTORS:
        print("No doctors are available.")
        return

    print("\n--- Doctor List ---")
    for doctor in data.DOCTORS:
        print("Doctor ID: " + str(doctor["id"]))
        print("Name:      " + str(doctor["name"]))

        if "specialty" in doctor:
            print("Specialty: " + str(doctor["specialty"]))
        elif "specialization" in doctor:
            print("Specialty: " + str(doctor["specialization"]))

        print("-------------------")
