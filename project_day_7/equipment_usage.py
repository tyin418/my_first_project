# equipment_usage.py

# Sample usage logs for medical equipment
usage_logs = {
    "X-ray Machine": 5,
    "MRI Scanner": 2,
    "Ultrasound": 3,
}

# Function to check usage
def check_usage(equipment):
    if usage_logs[equipment] > 4:
        print(f"⚠️ {equipment} is being overused! Consider maintenance.")
    else:
        print(f"✔️ {equipment} usage is normal.")

# Check usage for each machine
for machine in usage_logs:
    check_usage(machine)
