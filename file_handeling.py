# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is my first file in Python.\n")
    file.write("Learning Python is fun!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
