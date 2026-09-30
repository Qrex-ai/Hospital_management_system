# Community Clinic Record System

A beginner-level, terminal-based Python project for practicing functions, modules, loops, conditions, lists, dictionaries, and basic validation. It demonstrates patient registration and lookup, a doctor directory, appointment booking, simple bills, and a summary report.

> **Learning demo only:** use fictional information. This is not a real hospital product and has no authentication, privacy controls, medical decision support, or durable storage. Records live in Python lists and dictionaries and disappear when the program exits.

## Features

- Register and search patients; validate name, age, and phone format.
- View a small sample doctor directory.
- Book appointments for known patients and doctors.
- Create simple positive-amount bills.
- Display counts and demo revenue.
- Run unit tests using Python's built-in `unittest` module.

## Tools

- Python 3.8 or newer
- Standard library only; no external packages
- Git and GitHub for version control and submission

## Files

| Path | Purpose |
|---|---|
| `main.py` | Menu, user input, and program flow |
| `data.py` | In-memory lists, example doctors, and ID counters |
| `validation.py` | Input checks |
| `patients.py` | Patient registration and lookup |
| `doctors.py` | Doctor directory |
| `appointments.py` | Appointment rules and records |
| `billing.py` | Bill creation and history |
| `reports.py` | Counts and revenue summary |
| `tests/` | Unit tests for validation and record flows |
| `docs/` | Design diagrams and project report draft |
| `statement.md` | Problem, scope, users, and features |
| `SETUP_AND_EVALUATION.md` | Detailed 30-step guide |

## Run

1. Install Python 3 if needed and confirm `python --version` works.
2. Open a terminal in this folder.
3. Run `python main.py` (on some systems use `python3 main.py`).
4. Choose a menu number and enter fictional practice data.
5. Choose `0` to exit. The in-memory records reset.

## Test

From the project folder run:

```text
python -m unittest discover -s tests -v
```

The tests cover validation, patient registration and lookup, rejecting unknown patients, appointment creation, and bill validation. The tests also reset shared in-memory records between cases.

## Suggested manual walkthrough

1. Register `Riya`, age `19`, phone `9876543210`.
2. View patients and note the generated patient ID.
3. View doctors and choose a listed ID.
4. Book an appointment using `2026-09-29`.
5. Create a bill for `500` rupees.
6. View appointments, bills, and the summary.
7. Try an invalid phone, unknown patient ID, and non-date string; note the messages.
8. Exit and start again to observe that records do not persist.


## Limitations and next steps

The date checker checks format and simple month/day ranges, not actual calendar dates. The billing feature only totals entered demo charges; it is not financial software. Possible learning extensions: add editing/removal, prevent duplicate appointment slots, or explore file storage only after learning it in class and getting instructor approval.

