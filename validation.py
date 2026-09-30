"""Input validation for patient details and appointments dates."""

from datetime import datetime


def validate_patient(name, age_text, phone):
    if name == "":
        return "Name cannot be empty."
    if not age_text.isdigit():
        return "Age must be a whole number."
    age = int(age_text)
    if age < 0 or age > 120:
        return "Age must be between 0 and 120."
    if len(phone) != 10 or not phone.isdigit():
        return "Phone must contain exactly 10 digits."
    return ""


def validate_date(date_text):
    """Check the YYYY-MM-DD shape and basic month/day ranges."""
    parts = date_text.split("-")
    if len(parts) != 3:
        return False
    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    month_number = int(month)
    day_number = int(day)
    if month_number < 1 or month_number > 12:
        return False
    if day_number < 1 or day_number > 31:
        return False
    return True
