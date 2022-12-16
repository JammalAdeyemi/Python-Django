user = int(input("Enter a positive integer: "))

for i in range(1, user+1):
    print(str(i) * i)
for i in range(user-1, 0, -1):
    print(str(i) * i)