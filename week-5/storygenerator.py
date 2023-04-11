import random
from template import html_body_template, html_template, story_format, csv_format
from texts import firstNames, secondNames, story_starts, story_ends, consequences
import uuid

class Person:
    
    def __init__(self):

        self.uuid = uuid.uuid4()
        print(f"Person created: {self.uuid}")

        randomFirstName = getRandomListEntry(firstNames)
        randomSecondName = getRandomListEntry(secondNames)

        story_start = getRandomListEntry(story_starts)
        story_end   = getRandomListEntry(story_ends)
        consequence = getRandomListEntry(consequences)

        self.age = get_age(18, 121)

        self.story = story_format.format(
            story_start_var = story_start,
            story_end_var   = story_end,
            consequence_var = consequence
        )   

        self.fullRandomName = randomFirstName + " " + randomSecondName

    def __str__(self):
        return f"""Name: {self.fullRandomName}
        Age: {self.age}
        uuid: {self.uuid}
        Story: {self.story}"""

    def saveToCsv(self):

        csv_line = csv_format.format(
            fullRandomName = self.fullRandomName,
            age            = self.age,
            story          = self.story
        )

        with open("characters.csv", "a") as csv_file:
            csv_file.write(csv_line)


    def saveToHtml(self):
        html_body = html_body_template.format(
            fullRandomName = self.fullRandomName,
            age            = self.age,
            story          = self.story
        )
        html = html_template.format(body=html_body)

        file_name = f"characters_{self.uuid}.html"
        with open(file_name, "w") as html_file:
            html_file.write(html)
        


def getRandomListEntry(myList):
    numEntries = len(myList)
    randomIndex = random.randrange(0, numEntries)
    return myList[randomIndex]

def get_age(lower, higher):
    return random.randrange(lower, higher)


def main():
    loopRunning = True

    while(loopRunning):
        userinput = input("Get another character? (y/n):\n")
        userinput = userinput.upper()

        if(userinput == "YES" or userinput == "Y"):
            person = Person()
            print(person)
            person.saveToHtml()
        elif(userinput == "NO" or userinput == "N"):
            break
        else:
            print("Input not recognised, please type 'y' or 'n'!")
        


if __name__ == "__main__":
    main() 


