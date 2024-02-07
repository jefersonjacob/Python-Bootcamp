# Writing student ID numbers to a text file with dotted lines after each student
with open("reg_form.txt", 'w') as file:
    file.write("\nThe list of students and their ID numbers registered are:- \n\n")
    students_number = int(input("Enter the number of students registering: "))
    for i in range(students_number):
        student_number = input("Please enter the student ID number: ")
        file.write(f"The ID number of student {i+1} is {student_number}\n")
        file.write("." * 60)
        file.write("\n")
