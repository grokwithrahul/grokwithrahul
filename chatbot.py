import Functions.travelhandler as travel

cmdin = input("Hello, I am your virtual assistant. For flight booking, type 'Flight': ")

if cmdin == "Flight":
    location = input("Where do you want to fly to?: ")
    out = travel.flightsearch(location)
    print(out)