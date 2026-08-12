marks = [65, 72, 80] #The number/values of the marks
total = 0 #Intializing the total marks
for mark in marks: #This adds the marks all together
    total += mark
average = total / len(marks) #Calculates the average
if average >= 50: #This shows if the value of the average is below 50 or above 50
    print("Pass")
else:
    print("Fail")
