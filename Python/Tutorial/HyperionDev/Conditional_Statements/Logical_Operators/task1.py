#  Declare three variables called num1, num2 and num3. Assign each variable a number value.
num1 = 15
num2 = 25
num3 = 5

#  Now, compare num1 and num2 and display the larger value
if num1 > num2:
    larger_value = num1
else:
    larger_value = num2
print(f"The larger value is {larger_value}.")

# Next, determine whether num1 is odd or even and display the result.
if num1 % 2 == 0:
    print(f"{num1} is a even number")
else:
    print(f"{num1} is an odd number")

#  Next, write a conditional statement to sort the three numbers from largest to smallest.
if(num1 > num2 and num1 > num3): #find if num1 is the largest
    if(num2 > num3):
        l1 = num1
        l2 = num2
        l3 = num3
    else:
        l1 = num1
        l2 = num3
        l3 = num2
elif(num2 > num1 and num2 > num3): #check if num2 has the larger value
    if(num1 > num3):
        l1 = num2
        l2 = num1
        l3 = num3
    else:
        l1 = num2
        l2 = num3
        l3 = num1
else:
    if(num1 > num2): #else num3 is largest and find next largest
        l1 = num3
        l2 = num1
        l3 = num2
    else:
        l1 = num3
        l2 = num2
        l3 = num1

# print the sorted num
print("Sorted values from largest to smallest: ",l1, l2, l3)

