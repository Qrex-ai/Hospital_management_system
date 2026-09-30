"""Report generated from the current in-memory records."""

import data


def show_summary():
    total_revenue = 0
    for bill in data.BILLS:
        total_revenue += bill["amount"]
    print("\n--- Clinic Summary ---")
    print("Patients:", len(data.PATIENTS))
    print("Doctors:", len(data.DOCTORS))
    print("Appointments:", len(data.APPOINTMENTS))
    print("Bills:", len(data.BILLS))
    print("Demo revenue (INR):", total_revenue)
