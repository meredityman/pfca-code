import random


firstNames = [
    "Xriii",    # 0
    "Griggle",  # 1
    "Sldfy",    # 2
    "Wifrt"     # 3
]

secondNames = [
    "Troooble",
    "Scrungee",
    "Leeber",
    "Fromw"
]


def getRandomListEntry(myList):
    numEntries = len(myList)
    randomIndex = random.randrange(0, numEntries)
    return myList[randomIndex]

def main():
    # Get random first name
    randomFirstName = getRandomListEntry(firstNames)
    randomSecondName = getRandomListEntry(secondNames)

    fullRandomName = randomFirstName + " " + randomSecondName
    print(fullRandomName)


if __name__ == "__main__":
    main() 