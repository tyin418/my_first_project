# procedure_waitlist.py

import csv  # Import csv module

# Read the waitlist file
with open("procedure_waitlist.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    # Process each patient
    for row in reader:
        patient, procedure, days = row
        if int(days) > 20:
            print(f"⚠️ {patient} has been waiting too long for {procedure}.")
        else:
            print(f"✔️ {patient}'s {procedure} wait time is within limit.")
