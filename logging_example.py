import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
        return "Error: Cannot divide by zero."

print(divide(10, 2))
print(divide(10, 0))
