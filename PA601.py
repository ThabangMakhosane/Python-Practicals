import random

def createStudentID():
    StudentID = "ST"
    for i in range(6):
        Student_Num = random.randint(0, 9)
        StudentID += str(Student_Num)
    return StudentID
StudentID = createStudentID()
print(f"Student ID: {StudentID}")

code = random.randint(1000,9999)
print(f"Verification Code : {code}")