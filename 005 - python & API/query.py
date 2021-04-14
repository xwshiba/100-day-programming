from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
from random import randint

init()

ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="cyan")
print(colored_ascii)

import requests
url = "https://icanhazdadjoke.com/search"
joke = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": joke}
).json()

print(f"I've got {response['total_jokes']} jokes about {joke}. Here's one: ")

if response['total_jokes']>=1:
	num = randint(0, response['total_jokes']-1)
	print(response['results'][num]['joke'])
else:
	print("There's no joke!")



