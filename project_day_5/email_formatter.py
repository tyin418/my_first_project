# email_formatter.py

# List of employee names
employees = ["Alice Johnson", "Bob Smith", "Charlie Lee", "Diana Cruz"]

# Company domain
company_domain = "company.com"

# Function to generate emails
def generate_email(name):
    name = name.lower().replace(" ", ".")  # Convert to lowercase, replace spaces
    return f"{name}@{company_domain}"

# Create emails for all employees
email_list = [generate_email(emp) for emp in employees]

# Print formatted emails
print("Generated Email Addresses:")
for email in email_list:
    print(email)
