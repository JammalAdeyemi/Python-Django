# Write a program that will count the number of characters, words and lines in the input.txt file
# Your program should also count the total number of vowels (a, e, i, o and u) in the file.

with open('input.txt', 'r') as file:
  # Initialize the counters
  char_count = 0
  word_count = 0
  line_count = 0
  vowel_count = 0

  # Iterate over the lines in the file
  for line in file:
    line_count += 1
    words = line.split()
    word_count += len(words)

    # Iterate over the words in the line
    for word in words:
      char_count += len(word) # Increment the character counter by the number of characters in the word
      vowel_count += word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')

print(f"Number of characters: {char_count}")
print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")
print(f"Number of vowels: {vowel_count}")
