# physician_correspondence.py

# List of physician messages
messages = [
    {"Doctor": "Dr. Adams", "Specialist": "Radiologist", "Status": "Pending"},
    {"Doctor": "Dr. Lee", "Specialist": "Cardiologist", "Status": "Completed"},
    {"Doctor": "Dr. Patel", "Specialist": "Neurologist", "Status": "Pending"},
]

# Check messages and print updates
for msg in messages:
    if msg["Status"] == "Pending":
        print(f"⚠️ Follow-up needed: {msg['Doctor']} awaiting reply from {msg['Specialist']}.")
    else:
        print(f"✔️ Completed: {msg['Doctor']} received response from {msg['Specialist']}.")
