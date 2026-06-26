# Flow of program
# Sequential ✅
# Selection / Conditional ✅
# Iteration / Looping

# a = 10
# b = 20
# c = 30
# d = 40


# Loops
# for -> jaha meko pata hai kee mera code kittey bar chalega

# while -> voh loop hai jaha jab tak meri condition true naa hojaye tab tak chalega


# Take bill ammount and calculate final bill after discount
# less than 2500 - no discount
# more than 2500 - 15% discount 

# calculate total ammount if bills are
# 1800 -> 1800
# 3700 -> 3145

bill = float(input("Enter the bill -> "))
finalBill = None

if (bill > 2500):
    discount = bill * 0.15
    finalBill = bill - discount

else:
    finalBill = bill
    
print("Paaji Da Pind te swagat see")
print("Twada bill se")