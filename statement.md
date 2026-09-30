# Project Statement

## Problem statement

A small clinic may need a simple way to organize basic patient, appointment, and bill information. This project demonstrates a terminal-based workflow for entering and retrieving fictional records using core Python structures.

## Scope

The program supports patient registration and lookup, showing a fixed doctor list, booking appointments, creating basic bills, and viewing a summary. It is an educational prototype. It does not persist records between runs and is not suitable for real patient information or real clinical, billing, or administrative work.

## Target users

- A Python student learning modular programming and data structures.
- A reviewer who wants to inspect a small clinic workflow demonstration.

## High-level features

- Patient module: validate and register a patient; search by generated ID.
- Doctor module: view fictional sample doctors.
- Appointment module: check patient and doctor IDs and record a date.
- Billing module: record a positive whole-number demo bill.
- Reporting module: count records and add up demo bills.

## Assumptions

- One user operates the program through a terminal.
- All information is fictional and held in memory for one run.
- Dates are typed as `YYYY-MM-DD`; the basic checker is not a full calendar validator.
- The project is for learning, not deployment.
