# Create your own function that prints all the days of the week.
def days_of_the_week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        print(day)
        
days_of_the_week()


# Create your own function that takes in a sentence and replaces every second word with the word “Hello”
sentence = input("Enter a sentence: ")
def hello(sentence):
    words = sentence.split()
    for i in range(1, len(words), 2):
        words[i] = "Hello"
    print(" ".join(words))

hello(sentence)
