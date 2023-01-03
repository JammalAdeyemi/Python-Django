# Create a text file called numbers1.txt that contains Integers which are sorted from smallest to largest.
# Create another text file called numbers2.txt which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called all_numbers.txt
# All the numbers in all_numbers.txt should be sorted from smallest to largest.

# Open the first file in read mode
with open('numbers1.txt', 'r') as file1:
  # Read the contents of the file into a list
  numbers1 = [int(x) for x in file1.read().split()]

# Open the second file in read mode
with open('numbers2.txt', 'r') as file2:
  # Read the contents of the file into a list
  numbers2 = [int(x) for x in file2.read().split()]

# Combine the two lists and sort them
all_numbers = sorted(numbers1 + numbers2)

# Open the third file in write mode
with open('all_numbers.txt', 'w') as file3:
  # Write the sorted numbers to the file
  for number in all_numbers:
    file3.write(str(number) + '\n')

