def login():
    #Allows the user to log into the system.
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

def capture_student():
    #Captures student information and subject marks.
    student_name = input("Enter student name: ")
    programming = float(input("Enter Programming mark: "))
    database = float(input("Enter Database mark: "))
    web_development = float(input("Enter Web Development mark: "))

    return student_name, programming, database, web_development

def calculate_results(programming, database, web_development):
    #Calculates the total and average marks.
    total = programming + database + web_development
    average = total / 3

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, result

def display_results(student_name, total, average, result):
    #Displays the student's results.
    print("Student Results")
    print("Student Name:", student_name)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


def save_results(student_name, total, average, result):
    """Saves the student results to a file."""
    with open("student_results.txt", "a") as file:
        file.write(f"{student_name}, {total}, {average:.2f}, {result}\n")

    print("Results saved successfully.")


def read_results():
    #Reads and displays previously saved results.
    try:
        with open("student_results.txt", "r") as file:
            print("\n--- Saved Results ---")
            print(file.read())
    except FileNotFoundError:
        print("No saved results found.")


def display_menu():
    #Displays the main menu.
    print(" Student Results Management System")
    print("1. Capture Student")
    print("2. Read Results")
    print("3. Exit")


def main():
#Controls the main flow of the program.
    if login():
        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                student_name, programming, database, web_development = capture_student()

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


main()