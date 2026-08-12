student_number = "123456"
student_name = "John"
student_surname = "Doe"
student_age = 21
course = "Computer Science"
full_time_student = True
programming_mark = 85
database_mark = 64
web_development_mark = 78
registration_fee = 5000

totalmarks = programming_mark + database_mark + web_development_mark
print("Total marks :", totalmarks)
average_mark = totalmarks / 3
print("Average Mark :", average_mark)
if average_mark < 50:
    print("Your average mark is less than 50.")
max_mark = max(programming_mark, database_mark, web_development_mark)
print("Highest mark :", max_mark)
min_mark = min(web_development_mark, programming_mark, database_mark)
print("Lowest mark :", min_mark)
if programming_mark >= 40 and web_development_mark >= 40 and database_mark >= 40:
    print("You passed all of your modules")
if programming_mark >= 75 or web_development_mark >= 75 or database_mark >= 75:
    print("You have at least one distinction")
