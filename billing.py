"""Bill creation and history."""

from datetime import datetime

import data
from patients import find_patient


def create_bill(patient_id, amount_text):
    if find_patient(patient_id) is None:
        return "Bill not created: patient ID was not found."

    if not amount_text.isdigit() or int(amount_text) <= 0:
        return "Bill not created: amount must be a positive whole number."

    bill_id = "B" + str(data.NEXT_BILL_NUMBER).zfill(3)
    data.NEXT_BILL_NUMBER += 1

    bill = {
        "id": bill_id,
        "patient_id": patient_id,
        "amount_rupees": int(amount_text)
    }
    data.BILLS.append(bill)

    return (
        "Bill created successfully.\n"
        "Bill ID: " + bill["id"] + "\n"
        "Patient ID: " + bill["patient_id"] + "\n"
        "Amount: Rs. " + str(bill["amount_rupees"])
    )


def list_bills():
    if not data.BILLS:
        print("No bills have been created.")
        return

    print("\n--- Bill List ---")
    for bill in data.BILLS:
        print("Bill ID:    " + str(bill["id"]))
        print("Patient ID: " + str(bill["patient_id"]))

        if "amount_rupees" in bill:
            amount = bill["amount_rupees"]
        elif "amount" in bill:
            amount = bill["amount"]
        else:
            amount = "Not recorded"

        print("Amount:     Rs. " + str(amount))
        print("-----------------")