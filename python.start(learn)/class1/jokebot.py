import random

knock_knock = [
"Knock knock. Who’s there? Cow says. Cow says who? No, a cow says mooooo!",
"Knock knock. Who’s there? A little old lady. A little old lady who? All this time, I had no idea you could yodel.",
"Knock knock. Who’s there? Tank. Tank who? You’re welcome."
]

riddle_list = {
    "I’m tall when I’m young, and I’m short when I’m old. What am I? ":"A candle!",
    "What month of the year has 28 days? ":"All of them!",
    "What question can you never answer yes to? ":"Are you asleep yet?"
}

def jokebot(type):
    if type == "Knock Knock":
        jokenum = random.randint(0,2)
        out = knock_knock[jokenum]
        return(out)
    elif type == "Riddle":
        riddle, answer = random.choice(list(riddle_list.items()))
        return (riddle, answer)
