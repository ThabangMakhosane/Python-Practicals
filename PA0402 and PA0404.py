def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False


def capture_student():
    student_name = input("Enter student name: ")
    # Capture marks for each subject.
    programming = float(input("Enter Programming mark: "))
    database = float(input("Enter Database mark: "))
    web_development = float(input("Enter Web Development mark: "))

    return student_name, programming, database, web_development


def calculate_results(programming, database, web_development):

    # Calculate the total of all three subject marks.
    total = programming + database + web_development

    # Calculate the average mark.
    average = total / 3

    # Determine whether the student has passed.
    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, result


def display_results(student_name, total, average, result):
  
    print("\n--- Student Results ---")
    print("Student Name:", student_name)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


def save_results(student_name, total, average, result):

    # Open the file in append mode so previous results are not deleted.
    with open("student_results.txt", "a") as file:
        file.write(f"{student_name}, {total}, {average:.2f}, {result}\n")

    print("Results saved successfully.")


def read_results():
    
    try:
        with open("student_results.txt", "r") as file:
            print("\n--- Saved Results ---")
            print(file.read())
    except FileNotFoundError:
        print("No saved results found.")


def display_menu():
  
    print("Student Results Management System")
    print("1. Capture Student")
    print("2. Read Results")
    print("3. Exit")


def main():
   
    # The program only continues if the login is successful.
    if login():
        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                student_name, programming, database, web_development = capture_student()

                # Calculate the student's results.
                total, average, result = calculate_results(
                    programming,
                    database,
                    web_development
                )

                display_results(student_name, total, average, result)
                save_results(student_name, total, average, result)

            elif choice == "2":
                read_results()

            elif choice == "3":
                print("Program ended.")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the program by calling the main function.
main()