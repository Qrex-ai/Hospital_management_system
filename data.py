"""All the data for the hospital management system is stored in this file. This includes patients, appointments, bills, and doctors.
 The data is stored in lists and dictionaries for easy access and manipulation."""

PATIENTS = [
    {'id': "P001", "name": "Rahul kumar", "age": 30, "gender": "Male", "contact": "1235997890"},
    {'id': "P002", "name": "Jyoti Sharma", "age": 25, "gender": "Female", "contact": "9987654321"},
    {'id': "P003", "name": "Amita Patel", "age": 28, "gender": "Female", "contact": "9876543210"},
    {'id': "P004", "name": "Pratik Mehta", "age": 35, "gender": "Male", "contact": "9123456789"},
    {'id': "P005", "name": "Suresh Kumar", "age": 40, "gender": "Male", "contact": "9876543210"},
    {'id': "P006", "name": "Anjali Singh", "age": 32, "gender": "Female", "contact":"9988776655"},
    
]
APPOINTMENTS = [
    {"id": "A001", "patient_id": "P001", "doctor_id": "D001", "date": "2026-10-01", "time": "10:00 AM"},
    {"id": "A002", "patient_id": "P002", "doctor_id": "D002", "date": "2026-10-01", "time": "10:30 AM"},
    {"id": "A003", "patient_id": "P003", "doctor_id": "D003", "date": "2026-10-02", "time": "03:50 PM"},
    {"id": "A004", "patient_id": "P004", "doctor_id": "D004", "date": "2026-10-03", "time": "02:45 PM"},
    {"id": "A005", "patient_id": "P005", "doctor_id": "D002", "date": "2026-10-05", "time": "01:30 PM"},
    {"id": "A006", "patient_id": "P006", "doctor_id": "D004", "date": "2026-10-03", "time": "11:40 AM"},
]
BILLS = [
    {"id": "B001", "patient_id": "P001", "amount": 5070, "date": "2026-10-01"},
    {"id": "B002", "patient_id": "P002", "amount": 3090, "date": "2026-10-01"},
    {"id": "B003", "patient_id": "P003", "amount": 7809, "date": "2026-10-02"},
    {"id": "B004", "patient_id": "P004", "amount": 3060, "date": "2026-10-03"},
    {"id": "B005", "patient_id": "P005", "amount": 6308, "date": "2026-10-05"},
    {"id": "B006", "patient_id": "P006", "amount": 8560, "date": "2026-10-03"},
]

DOCTORS = [
    {"id": "D001", "name": "Dr. Asha Rao", "specialty": "General Medicine"},
    {"id": "D002", "name": "Dr. Kabir Shah", "specialty": "Paediatrics"},
    {"id": "D003", "name": "Dr. Neha Iyer", "specialty": "Dentistry"},
    {"id": "D004", "name": "Dr. Ramesh Gupta", "specialty": "Cardiology"},
]

NEXT_PATIENT_NUMBER = 7
NEXT_APPOINTMENT_NUMBER = 7
NEXT_BILL_NUMBER = 7
