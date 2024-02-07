
user_number = float(input("Enter a number of your choice: "))
sum1 = 0
i = 0
while user_number != -1:
    sum1 += user_number # new sum1 value = sum1 current value (starts with 0) + user_number
    i += 1 # new i value = i current value (starts with 0) + 1 
    user_number = float(input("Enter a number of your choice: "))
average = sum1 / i 
print(f"The average of the numbers entered are {average}, total numbers entered are {i} and sum of all numbers entered are {sum1}")