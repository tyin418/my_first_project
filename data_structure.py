# Initialize the list of students
students = []

# Function to add a student
def add_student(name, grade):
    students.append({"name": name, "grade": grade})

# Function to calculate the average grade
def calculate_average():
    total = sum(student['grade'] for student in students)
    return total / len(students) if students else 0

# Function to find the student with the highest grade
def find_highest_grade():
    if not students:
        return None
    return max(students, key=lambda student: student['grade'])

# Function to find the student with the lowest grade
def find_lowest_grade():
    if not students:
        return None
    return min(students, key=lambda student: student['grade'])

# Main program loop
print("Student Grade Tracker")
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average Grade")
    print("4. Find Highest Grade")
    print("5. Find Lowest Grade")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        name = input("Enter the student's name: ")
        try:
            grade = float(input(f"Enter the grade for {name}: "))
            if 0 <= grade <= 100:
                add_student(name, grade)
                print(f"{name} added with a grade of {grade}.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number for the grade.")
    
    elif choice == "2":
        if students:
            print("\nList of Students:")
            for student in students:
                print(f"Name: {student['name']}, Grade: {student['grade']}")
        else:
            print("No students in the list.")
    
    elif choice == "3":
        average = calculate_average()
        print(f"\nThe average grade is: {average:.2f}")
    
    elif choice == "4":
        highest = find_highest_grade()
        if highest:
            print(f"\nThe highest grade is {highest['grade']} by {highest['name']}.")
        else:
            print("No students in the list.")
    
    elif choice == "5":
        lowest = find_lowest_grade()
        if lowest:
            print(f"\nThe lowest grade is {lowest['grade']} by {lowest['name']}.")
        else:
            print("No students in the list.")
    
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select from the menu options.")
