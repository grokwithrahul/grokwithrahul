#import class1.jokebot
import time

name = input("Hello, I am your virtual assistant. What is your name?: ")
print("Hello "+name+", I am ChatBot.")

time.sleep(1.5)

while True:
    cmdin = input("To search for flights, type in 'Flight'. To search for Trains, type in 'Train'. To hear a joke, type in 'Joke': ")
    if cmdin == "Flight":
        location = input("Where do you want to fly to?: ")
#        out = travel.flightsearch(location)
#        print(out)
    elif cmdin == "Train":
        location = input("Where do you want to travel to?: ")
#        out = travel.trainsearch(location)
#        print(out)
