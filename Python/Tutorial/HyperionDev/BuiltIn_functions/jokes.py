# You are going to create a random joke generator using Python’s random module. 
import random

# Create a list of jokes.

jokes = [
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "What do you call a bear with no teeth? A gummy bear.",
    "What do you call a cow with two legs? Lean beef.",
    "What did the big flower say to the little flower? 'Hey, bud!'",
    "Why was the math book sad? It had too many problems.",
    "What do you call a cow jumping over a barbed wire fence? Beef jerky.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "What do you get when you cross a sheep and a kangaroo? A woolly jumper.",
    "Why couldn't the leopard play hide and seek? Because he was always spotted.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What did the zero say to the eight? Nice belt.",
    "What do you call a cow with no legs? Ground beef.",
    "What did the duck say when it bought lipstick? 'Put it on my bill.'",
    "Why was the computer cold? Because it left its Windows open."
]

# Use the random module to display a random joke each time the code runs.
joke = random.choice(jokes)
print(joke)
