import csv  # Read medicine stock data

with open("medicine_stock.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        if len(row) < 2:
            continue  # Skip invalid rows

        medicine, stock = row[:2]
        
        try:
            stock = int(stock)  # Convert to integer
            print(f"⚠️ {medicine} is out of stock!" if stock == 0 else f"{medicine}: {stock} units available.")
        except ValueError:
            print(f"❌ Invalid stock value '{stock}' for {medicine}. Check CSV file.")
