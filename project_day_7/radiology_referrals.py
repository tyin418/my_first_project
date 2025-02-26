# radiology_referral.py

import csv  # Import the csv module to read patient referrals

# Open the referral file and read data
with open("radiology_referrals.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Loop through referrals
    for row in reader:
        patient, test, date = row  # Extract each column
        print(f"Referral: {patient} needs a {test} on {date}.")
