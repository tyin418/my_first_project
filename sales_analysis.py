# Sales Analysis with CSV
import csv

# Write Sales Data to a File
with open("sales_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Product", "Quantity", "Price"])
    writer.writerow(["2025-01-23", "Laptop", 2, 1500])
    writer.writerow(["2025-01-23", "Mouse", 5, 25])
    writer.writerow(["2025-01-24", "Keyboard", 3, 45])

# Read Sales Data and Analyze
with open("sales_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    total_revenue = 0
    for row in reader:
        quantity = int(row[2])
        price = float(row[3])
        total_revenue += quantity * price
    print(f"Total Revenue: ${total_revenue:.2f}")
