def capture_student():
    student_num = input("Enter Student number: ")
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course name: ")
    prog_mark = int(input("Enter Programming mark: "))
    db_mark = int(input("Enter Database mark: "))
    web_mark = int(input("Enter Web development mark: "))
    

    print("STUDENT INFORMATION")
    print(f"Student Number: {student_num}")
    print(f"Student Name: {name} {surname}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Programming Mark: {prog_mark}")
    print(f"Database Mark: {db_mark}")
    print(f"Web Development Mark: {web_mark}")

# Call the function to test it
capture_student()
