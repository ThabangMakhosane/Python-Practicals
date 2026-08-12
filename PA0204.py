# Store subjects and marks in a dictionary
marks_data = {
    "Programming": 78,
    "Database": 65,
    "Web Development": 72
}

# Initialize tracking variables
total_mark = 0
subject_count = 0

# Loop through the dictionary to calculate totals
for subject, mark in marks_data.items():
    total_mark += mark
    subject_count += 1

# Calculate the average mark
average_mark = total_mark / subject_count

# Display the results
print(f"Total Mark: {total_mark}")
print(f"Number of Subjects: {subject_count}")
print(f"Average Mark: {average_mark:.2f}")
