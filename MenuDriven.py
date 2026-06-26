# Menu Driven Programs 
# Create a Simple Calculator.

ch = "y"

while (ch == "y"):

    print("Welcome to Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter Your Choice "))
    res = None

    if (choice == 1):
        n1 = int(input("Enter Your First Number "))
        n2 = int(input("Enter Your Second Number "))
        res = n1 + n2

    elif (choice == 2):
        n1 = int(input("Enter Your First Number "))
        n2 = int(input("Enter Your Second Number "))
        res = n1 - n2
        
    elif (choice == 3):
        n1 = int(input("Enter Your First Number "))
        n2 = int(input("Enter Your Second Number "))
        res = n1 * n2
        
    elif (choice == 4):
        n1 = int(input("Enter Your First Number "))
        n2 = int(input("Enter Your Second Number "))
        res = n1 / n2   

    else:
        print("InValid")
    
    
    print("Result is",res)
    
    ch = input("Do You Wsant To Do Again? [y/n] ")