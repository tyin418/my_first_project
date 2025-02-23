# Visualize Sales Data with Matplotlib
import matplotlib.pyplot as plt

# Sales Data
products = ["Laptop", "Mouse", "Keyboard"]
quantities = [2, 5, 3]
prices = [1500, 25, 45]

# Calculate Total Revenue per Product
revenues = [quantities[i] * prices[i] for i in range(len(products))]

# Plot the Data
plt.bar(products, revenues, color="blue")
plt.title("Sales Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.show()
