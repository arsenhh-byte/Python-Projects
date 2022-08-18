sum =0 
for even in range(0,101, 2):
    sum += even
print (sum)

total = 0
for number in range(0,101):
    # You can't use the / in the below function because logically it will take the numbers that are not divisible by 2 and numbers that have a reminder.
    if number % 2 == 0:
        total += number
print (total)