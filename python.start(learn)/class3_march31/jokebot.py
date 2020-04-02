import random
"""
This is an import function. Python code in one file can access code in another module by importing it. Random is a
module which allows the user to generate random numbers, choices, etc.
"""


knock_knock = [
"Knock knock. Who’s there? Cow says. Cow says who? No, a cow says mooooo!",
"Knock knock. Who’s there? A little old lady. A little old lady who? All this time, I had no idea you could yodel.",
"Knock knock. Who’s there? Tank. Tank who? You’re welcome."
]
"""
This is a list. Lists(aka arrays) are data structures that are changeable, ordered sequence of elements. Each element 
or value that is inside of a list is called an item.

Lists start from 0. So the first item in a list is the 0th item.
To access an item in a list, use listname[itemnum]
For example, if you want to access the first item in the list knock_knock, you would do knock_knock[0]

You can add a variable to replace what is in []. 
e.g.
n = 8

item = listname[n]
"""


riddle_dict = {
    "I’m tall when I’m young, and I’m short when I’m old. What am I? ":"A candle!",
    "What month of the year has 28 days? ":"All of them!",
    "What question can you never answer yes to? ":"Are you asleep yet?"
}
"""
This is a dictionary. The dictionary is divided into pairs. The first part of a pair in a dictionary is called a key.
The second is called a value. So, pairs in dictionaries are called key-value pairs.

You can access the value of a pair if you have a key. This is useful in our situation because we can get the answer to a
riddle (in this case the value) if we have the riddle (in this case the key).

Look at https://docs.python.org/3/tutorial/datastructures.html#dictionaries for more info.
"""


def jokebot(type):
    if type == "Knock Knock":
        jokenum = random.randint(0,2)
        out = knock_knock[jokenum]
        return(out)
    elif type == "Riddle":
        riddle, answer = random.choice(list(riddle_dict.items())) #Look at the randoom module's documentation
        return(riddle, answer)
