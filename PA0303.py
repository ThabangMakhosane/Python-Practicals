from datetime import datetime

def save_results():
    # Define the student information based on the example provided
    student_number = "ST001"
    student_name = "Thabo Molefe"
    course = "Software Development"
    
    # Subject marks
    programming_mark = 78
    database_mark = 65
    web_dev_mark = 72
    
    # Calculations
    total_marks = programming_mark + database_mark + web_dev_mark
    average_mark = total_marks / 3
    final_result = "Competent" if average_mark >= 50 else "Not Yet Competent"
    
    # Format the current date as 'DD Month YYYY' (e.g., 14 August 2026)
    date_saved = datetime.now().strftime("%d %B %Y")
    
    # Open the file in write mode using file = open(...) as requested
    file = open("student_results.txt", "w")
    
    # Write the formatted information to the file
    file.write(f"Student Number: {student_number}\n")
    file.write(f"Student Name: {student_name}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Programming: {programming_mark}\n")
    file.write(f"Database: {database_mark}\n")
    file.write(f"Web Development: {web_dev_mark}\n")
    file.write(f"Total: {total_marks}\n")
    file.write(f"Average: {average_mark:.2f}\n")
    file.write(f"Result: {final_result}\n")
    file.write(f"Date Saved: {date_saved}\n")
    
    # Close the file correctly
    file.close()
    print("Results successfully saved to student_results.txt\n")

def read_results():
    # Open the text file in read mode
    file = open("student_results.txt", "r")
    
    # Read its contents
    file_contents = file.read()
    
    # Display the information on the console
    print("--- Displaying File Contents ---")
    print(file_contents)
    
    # Close the file correctly
    file.close()

# Execute the functions to demonstrate functionality
save_results()
read_results()
