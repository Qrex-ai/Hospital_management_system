"""Appointment booking and listing."""

import data
from patients import find_patient
from validation import validate_date


def doctor_exists(doctor_id):
    for doctor in data.DOCTORS:
        if doctor["id"] == doctor_id:
            return True
    return False

from datetime import datetime

def book_appointment(patient_id, doctor_id, visit_date, visit_time):
    if find_patient(patient_id) is None:
        return "Appointment not booked: patient ID was not found."

    if not doctor_exists(doctor_id):
        return "Appointment not booked: doctor ID was not found."

    if not validate_date(visit_date):
        return "Appointment not booked: use a YYYY-MM-DD date."

    appointment_id = "A" + str(data.NEXT_APPOINTMENT_NUMBER).zfill(3)
    data.NEXT_APPOINTMENT_NUMBER += 1

    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": visit_date,
        "time": visit_time
    }
    data.APPOINTMENTS.append(appointment)

    return (
        "Appointment booked successfully.\n"
        "Appointment ID: " + appointment["id"] + "\n"
        "Patient ID: " + appointment["patient_id"] + "\n"
        "Doctor ID: " + appointment["doctor_id"] + "\n"
        "Date: " + appointment["date"] + "\n"
        "Time: " + appointment["time"]
    )


def list_appointments():
    if not data.APPOINTMENTS:
        print("No appointments have been booked.")
        return

    print("\n--- Appointment List ---")
    for appointment in data.APPOINTMENTS:
        print("Appointment ID: " + str(appointment["id"]))
        print("Patient ID:     " + str(appointment["patient_id"]))
        print("Doctor ID:      " + str(appointment["doctor_id"]))
        print("Date:           " + str(appointment["date"]))

        if "time" in appointment:
            print("Time:           " + str(appointment["time"]))

        print("------------------------")