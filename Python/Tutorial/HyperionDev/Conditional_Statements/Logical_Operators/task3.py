#  Design a program that determines the award a person competing in a triathlon will receive
swimming = int(input("Enter time taken for swimming in minutes: "))
print(f"Time taken for Swimming task: {swimming}")

cycling = int(input("\nEnter time taken for cycling in minutes: "))
print(f"Time taken for Cycling task: {cycling}")

running = int(input("\nEnter time taken for running in minutes: "))
print(f"Time taken for Running task: {running}")

Total_time = swimming + cycling + running
print(f"Total time taken for the triathlon: {Total_time}")

if (Total_time < 100):
    print("Provincial Colors")
elif (Total_time > 100 and Total_time <= 105):
    print("Provincial Half Colors")
elif (Total_time > 105 and Total_time <= 110):
    print("Provincial Scroll")
else:
    print("No award")

