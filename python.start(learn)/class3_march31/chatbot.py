from . import jokebot as jb
"""
Over here we are importing the file jokebot from the folder class3_march31 as jb. So instead of
typing jokebot() we can type in jb()

We have imported a module from a different file in the same folder.
"""


import time

name = input("Hello, I am your virtual assistant. What is your name?: ")
print("Hello ",name,", I am ChatBot.")

time.sleep(1.5)

while True:
    cmdin = input("To hear a joke, type in 'Joke': ")
    if cmdin == "Joke" or cmdin == "joke":
        type_of_joke = input("Do you want to hear a 'Riddle' or a 'Knock Knock'?: ")
        out = jb.jokebot(type_of_joke) # We are using jokebot.py's (which we imported as jb) jokebot function
        print(out)
    else:
        out = "Input a valid command."
        print(out)
