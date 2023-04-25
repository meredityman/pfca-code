story_format = "Started life as {story_start_var} and later {story_end_var}. As a result they feels {consequence_var}."

csv_format = '"{fullRandomName}","{age}","{story}"\n'

html_body_template = """
    <div class="id-card">
        <img src="{image_path}" alt="{fullRandomName}">
        <div class="name">Name: {fullRandomName}</div>
        <div class="age">Age: {age}</div>
        <div class="description">Details:<br>{story}</div>
    </div>

"""

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Character Card</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .id-card {{
            width: 350px;
            height: 500px;
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .id-card img {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #000;
        }}
        .name, .age, .description {{
            width: 100%;
            text-align: center;
            margin: 10px 0;
            background-color: #fff;
            border: 1px solid #000;
            padding: 8px;
        }}
    </style>
</head>
<body>
{body}
</body>
</html>
"""
