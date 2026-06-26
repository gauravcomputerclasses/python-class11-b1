# if-elif-else ladder -> isme hum multiple conditions pe kaam karte hai.

# GRADE SYSTEM
# 91-100 -> A
# 81-90 -> B
# 71-80 -> C
# 61-70 -> D
# LESS THAN 60 -> F

# INPUT MARKS OF 5 SUBJECTS AND CALACULATE PERCENTAGE AND GRADE

grade = None
sub1 = int(input("Enter Marks For Subject 1 -> "))
sub2 = int(input("Enter Marks For Subject 2 -> "))
sub3 = int(input("Enter Marks For Subject 3 -> "))
sub4 = int(input("Enter Marks For Subject 4 -> "))
sub5 = int(input("Enter Marks For Subject 5 -> "))

# obtained marks/ total marks * 100

percentage = ((sub1 + sub2 + sub3 + sub4 + sub5) / 500) * 100

if (percentage >= 91  and percentage <= 100):
    grade = "A"

elif (percentage >= 81 and percentage <= 90):
    grade = "B"
    
elif (percentage >= 71 and percentage <= 80):
    grade = "C"
    
elif (percentage >= 61 and percentage <= 70):
    grade = "D"

else:
    grade = "F"

print("You Got",percentage,"%")
print("You Got Grade",grade)

