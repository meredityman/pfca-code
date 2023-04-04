import random


firstNames = [
    "Zorin",
    "Valtor",
    "Nexa",
    "Xandar",
    "Qezal",
    "Tazra",
    "Krynn",
    "Wryx",
    "Yalara",
    "Gornax",
    "Nalax",
    "Felnor",
    "Zeltrax",
    "Traxx",
    "Rynex",
    "Vexon",
    "Kylera",
    "Jaxar",
    "Zylar",
    "Zethron"
]

secondNames = [
    "Troooble",
    "Scrungee",
    "Leeber",
    "Fromw"
]


story_starts = [
    "a plumber", 
    "an astronaut", 
    "a loner"
]
story_ends   = [
    "became a sardine", 
    "took up tufting as a hobby", 
    "ate a whole box of donuts"
]
consequences = [
    "deeply contented", 
    "inclines to enter the crypto-marketing space", 
    "increasingly obsessed with flower arranging"
]


story_format = "Started life as {story_start_var} and later {story_end_var}. As a result they feels {consequence_var}."


def getRandomListEntry(myList):
    numEntries = len(myList)
    randomIndex = random.randrange(0, numEntries)
    return myList[randomIndex]

def get_age(lower, higher):
    return random.randrange(lower, higher)


def get_charachter():
    # Get random first name
    randomFirstName = getRandomListEntry(firstNames)
    randomSecondName = getRandomListEntry(secondNames)

    story_start = getRandomListEntry(story_starts)
    story_end   = getRandomListEntry(story_ends)
    consequence = getRandomListEntry(consequences)

    age = get_age(18, 121)

    story = story_format.format(
        story_start_var = story_start,
        story_end_var   = story_end,
        consequence_var = consequence
    )   

    fullRandomName = randomFirstName + " " + randomSecondName

    print(f"Name: {fullRandomName}")
    print(f"Age: {age}")
    print(f"Story:\n{story}")



def main():
    loopRunning = True

    while(loopRunning):
        input("Get another character?")
        get_charachter()


if __name__ == "__main__":
    age = get_age(18, 121)
    main() 