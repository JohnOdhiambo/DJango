#Student Dataset
students = [
    {"name": "Hilda", "age": 20, "grade": 90.2},
    {"name": "Joan", "age": 22, "grade": 78.0},
    {"name": "Charlie", "age": 21, "grade": 92.3},
    {"name": "Jay", "age": 23, "grade": 88.9},
    {"name": "Eve", "age": 20, "grade": 73.5}
]

#Function to display the students
def display_students(students_list):
    """Display the list of students with their details."""
    if not students_list:
        print("No students to display.")
    else:
        print("\nList of Students:")
        for student in students_list:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

#Function to filter students based on grade threshold
def filter_students(students_list, threshold):
    """Return students with grades above the given threshold."""
    return [student for student in students_list if student['grade'] > threshold]

#Function to calculate average grade of the srudents
def calculate_average_grade(students_list):
    """Calculate and return the average grade of all students."""
    total = sum(student['grade'] for student in students_list)
    return total / len(students_list) if students_list else 0

# Main program
def main():
    print("Welcome to the Student Data Analysis Program!")
    
    # 1.Get grade threshold from the user input
    try:
        threshold = float(input("Enter a grade threshold to filter students by grade: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # 2.Prompt the user to enter what they want to view
    print("\nChoose an option:")
    print("1. View all students")
    print("2. View students above the specified grade threshold")
    print("3. View the average grade of all students")
    
    choice = input("Enter the number of your choice: ")
    
    # 3.Conditional Logic for Displaying Data
    if choice == "1":
        print("\n-- All Students --")
        display_students(students)
    elif choice == "2":
        print(f"\n-- Students with Grade Above {threshold} --")
        filtered_students = filter_students(students, threshold)
        display_students(filtered_students)
    elif choice == "3":
        avg = calculate_average_grade(students)
        print(f"\nThe average grade of all students is: {avg:.2f}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main program
if __name__ == "__main__":
    main()

