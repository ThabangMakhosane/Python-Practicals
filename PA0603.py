import os
from datetime import datetime
import math
# Check whether student_results.txt exists.
file_exists = os.path.exists("student_results.txt")
print(f"Does file exist? {file_exists}")

# Display the current working directory.
current_dir = os.getcwd()
print(f"Current Working Directory: {current_dir}")

# Create a folder named student_records when it does not exist.
if not os.path.exists("student_records"):
    os.mkdir("student_records")

#  Display the current date and time.
current_datetime = datetime.now()
print(f"Current Date and Time: {current_datetime}")

#  Save the date on which the student results were created.
# (Assuming today's date for this example)
creation_date = datetime.now()

#  Format the date as: 04 August 2026
formatted_date = creation_date.strftime("%d %B %Y")
print(f"Formatted Date: {formatted_date}")

# Sample values for demonstration
average_mark = 74.3
total_mark = 450.0

# Round the average mark upwards using math.ceil().
rounded_up = math.ceil(average_mark)
print(f"Rounded Up: {rounded_up}")

# Round the average downwards using math.floor().
rounded_down = math.floor(average_mark)
print(f"Rounded Down: {rounded_down}")

# Calculate the square root of the total mark using math.sqrt().
square_root = math.sqrt(total_mark)
print(f"Square Root of Total Mark: {square_root}")
