# PA 0503: Create error handling code

def process_student_information():
    print("--- Student Information Processing ---")
    
    try:
        # 1. Handle non-numeric input for age
        age_input = input("Enter student age: ")
        age = int(age_input)  # Raises ValueError if letters are entered
        
        # 2. Handle non-numeric input for mark
        mark_input = input("Enter student mark: ")
        mark = float(mark_input)  # Raises ValueError if letters are entered
        
        # 3 & 4. Handle marks below 0 or above 100
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")
            
        # 5. Handle a missing results file
        filename = input("Enter results filename to open (e.g., results.txt): ")
        with open(filename, "r") as file:
            content = file.read()
            print("File loaded successfully.")
            
        # 6. Handle division by zero where applicable
        # Example scenario: Calculating average mark per year of age
        if age == 0:
            raise ZeroDivisionError("Age cannot be zero when performing division operations.")
        average_per_year = mark / age
        print(f"Average mark score per year of age: {average_per_year:.2f}")

    except ValueError as error:
        # Catches letters-instead-of-numbers and out-of-range marks
        print(f"Invalid input: {error}")
        
    except FileNotFoundError:
        # Catches missing files
        print("Error: The requested results file does not exist.")
        
    except ZeroDivisionError as error:
        # Catches division by zero
        print(f"Mathematical Error: {error}")
        
    else:
        # Executes only if no exceptions were raised
        print("All data accepted and processed with no errors.")
        
    finally:
        # Executes no matter what
        print("Student information process completed.")

# Run the program
if __name__ == "__main__":
    process_student_information()
