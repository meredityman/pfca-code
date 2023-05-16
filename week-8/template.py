story_format = "Started life as {story_start_var} and later {story_end_var}. As a result they feels {consequence_var}."

csv_format = '"{fullRandomName}","{age}","{story}"\n'

html_body_template = """
    <div class="character-info">
        <img src="{imagePath}">
        <p class="character-name">{fullRandomName}</p>
        <p>Age: {age}</p>
        <div class="character-story">
            <p>{story}</p>
        </div>
    </div>
"""

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Character Card</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Set A5 page size */
        @page {{
            size: A5;
        }}
        /* Set card dimensions and margin */
        body {{
            width: 148mm;
            height: 210mm;
            margin: 0;
            padding: 10mm;
        }}
        /* Style for character information */
        .character-info {{
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
        }}
        /* Style for character name */
        .character-name {{
            font-weight: bold;
        }}
        /* Style for character background story */
        .character-story {{
            margin-top: 10mm;
        }}
    </style>
</head>
<body>
{body}
</body>
</html>
"""

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
    "inclines to enter the crypto-marketing space, not a great idea", 
    "increasingly obsessed with flower arranging"
]
