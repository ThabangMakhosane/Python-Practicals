def process_student_data():
    print("--- Student Information Section ---")
    
    # Requirements 1-4: Input Validation
    try:
        # 1. Handle letters instead of an age
        age_input = input("Enter student age: ")
        age = int(age_input) 
        
        # 2. Handle letters instead of a mark
        mark_input = input("Enter student mark (0-100): ")
        mark = float(mark_input)
        
        # 3 & 4. Handle marks below 0 or above 100
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100 inclusive.")

    except ValueError as e:
        # Catches conversion errors (letters to numbers) and custom raised errors
        print(f"Input Error: {e}")
        return  # Stop execution if inputs are invalid
        
    else:
        # Executes only if no exceptions were raised in the try block
        print(f"Inputs accepted successfully. Age: {age}, Mark: {mark}")

    # Requirement 5: Missing results file
    file_name = "student_results.txt"
    file_ptr = None
    
    try:
        # Attempting to read a file that might not exist
        file_ptr = open(file_name, "r")
        content = file_ptr.read()
        print("File contents loaded successfully.")
    except FileNotFoundError:
        print(f"File Error: The file '{file_name}' does not exist.")
    else:
        print("Data processed from file successfully.")
    finally:
        # Always executes to ensure system resources are safely closed
        if file_ptr:
            file_ptr.close()
            print("File resource safely closed.")

    # Requirement 6: Division by zero where applicable
    # Example scenario: Calculating average mark per assignment completed
    try:
        assignments_completed = int(input("Enter number of completed assignments: "))
        average_per_assignment = mark / assignments_completed
    except ZeroDivisionError:
        print("Math Error: Cannot divide by zero assignments.")
    except ValueError:
        print("Input Error: Assignments must be a whole number.")
    else:
        print(f"Average mark per assignment: {average_per_assignment:.2f}")
    finally:
        print("--- Section Processing Complete ---")

# Run the program
process_student_data()
