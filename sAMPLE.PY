# if - else

# if else humare conditional statement hai. 

# if -> agr condition ka overall answer true hota hai toh yeh kaam karo
# SYNTAX
# if (<Condition>):
    # statements
    
# check if age is greater than 18 or not. if it is greater then print "You are eligible to vote"

age = int(input("Enter your age -> "))

if (age >= 18):
    print("Your are eligible to vote")
    
elif (age <= 0):
    print("ERORRRRRR")
    print("Invaliddddd Age")

else:
    print("Your are under age.")