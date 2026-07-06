waterConsumed = int(input("Enter number of liters -> "))
totalBill = 0

if (waterConsumed <= 100):
    totalBill = 100

# 200 L
elif (waterConsumed >=101 and waterConsumed <= 300):
    totalBill = 100 + (waterConsumed-100) * 2

else:
    totalBill = 100 + 400 + (waterConsumed - 300) * 5
    
print("Your Total Bill is",totalBill)