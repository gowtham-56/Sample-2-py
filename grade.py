# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

# Sample data: dictionary of student names and their list of grades
students_grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 90, 93]
}

# Calculate average grades for each student
average_grades = {student: calculate_average(grades) for student, grades in students_grades.items()}

# Write results to a text file
with open("average_grades.txt", "w") as file:
    file.write("Student Average Grades:\n")
    file.write("=======================\n")
    for student, average in average_grades.items():
        file.write(f"{student}: {average:.2f}\n")

print("Average grades have been calculated and written to 'average_grades.txt'")