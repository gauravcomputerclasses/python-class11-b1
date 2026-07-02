mini = midi = maxi = None

num1 = int(input("Enter number 1 -> "))
num2 = int(input("Enter number 2 -> "))
num3 = int(input("Enter number 3 -> "))

# mei abhi ke liye num 1 ko maxi maan raha hu

if (num1 > num2 and num1 > num3):
    if (num2 > num3):
        mini,midi,maxi = num3,num2,num1
    else:
        mini,midi,maxi = num2,num3,num1

# ab mai num 2 ko maxi maan raha hu

elif (num2 > num1 and num2 > num3):
    if (num1 > num3):
        mini,midi,maxi = num3,num1,num2
    else:
        mini,midi,maxi = num1,num3,num2

# ab mere paas kehne ko bas yahi hai kee agr mere do nalayak number chote nikal gaye mei toh mera sabse aakhri number hee bada hai, toh meko else use karna padega, iska matlab num 3 is maxi

else:
    if(num1 > num2):
        mini,midi,maxi = num2,num1,num3
    else:
        mini,midi,maxi = num1,num2,num3
        
print(mini,midi,maxi)