import random
from template import html_body_template, html_template, story_format, csv_format
from texts import firstNames, secondNames, story_starts, story_ends, consequences


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

    # print(f"Name: {fullRandomName}")
    # print(f"Age: {age}")
    # print(f"Story:\n{story}")

    csv_line = csv_format.format(
        fullRandomName=fullRandomName,
        age=age,
        story=story
    )
    print(csv_line)

    with open("characters.csv", "a") as csv_file:
        csv_file.write(csv_line)


    # HTML
    html_body = html_body_template.format(
        fullRandomName=fullRandomName,
        age=age,
        story=story
    )
    html = html_template.format(body=html_body)

    with open("characters.html", "w") as html_file:
        html_file.write(html)



def main():
    loopRunning = True

    while(loopRunning):
        userinput = input("Get another character? (y/n):\n")
        userinput = userinput.upper()

        if(userinput == "YES" or userinput == "Y"):
            get_charachter()
        elif(userinput == "NO" or userinput == "N"):
            break
        else:
            print("Input not recognised, please type 'y' or 'n'!")
        


if __name__ == "__main__":
    main() 


