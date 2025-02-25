# appointment_reminder.py

import csv  # Import csv module to read patient appointments

# Read the CSV file
with open("appointments.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Loop through each patient appointment
    for row in reader:
        patient, date, time = row  # Extract data from each row
        print(f"Reminder: {patient}, you have an appointment on {date} at {time}.")
