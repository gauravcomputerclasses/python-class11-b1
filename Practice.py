# take time in minutes and then convert it into hours and minutes

# input - 90 mins
# output - 1 hour 30 minutes

# take input in seconds and print in the format, hours minutes and seconds

# input : 4560
# output : 1 hour 16 minutes 0 seconds


seconds = int(input("Enter Time in seconds "))


time = seconds // 60 #mins

hours = time // 60
mins = time % 60
seconds = seconds % 60

print(time,"in hours and minutes is",hours,"hours",mins,"minutes",seconds,"seconds")