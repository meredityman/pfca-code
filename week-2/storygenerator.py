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

# Get random first name
firstNameNum = len(firstNames)
firstNameIndex = random.randrange(0,firstNameNum)
randomFirstName = firstNames[firstNameIndex]
print(firstNameNum, firstNameIndex, firstNames[firstNameIndex])


# Get random second name
secondNameNum = len(secondNames)  
secondNameIndex = random.randrange(0,secondNameNum)
randomSecondName = secondNames[secondNameIndex]
print(secondNameNum, secondNameIndex, secondNames[secondNameIndex])


fullRandomName = randomFirstName + " " + randomSecondName
print(fullRandomName)