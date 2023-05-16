from PIL import Image, ImageDraw, ImageFont


def get_card_image(image, fullRandomName, age):
    width, height =  (1720,1080)

    portrait = image.convert("RGBA")

    print(f"Making image {width}x{height}")
    background = Image.new(mode="RGBA", size=(width, height), color=(0, 0, 0, 0))

    x, y = (150, 200)
    w, h = (600, 600)
    portrait = portrait.resize((w, h))

    background.paste(portrait, box=(x, y, x + w, y + h))

    draw = ImageDraw.Draw(background)

    font       = ImageFont.truetype("Arial", 52)
    big_font   = ImageFont.truetype("Arial", 68)
    text_color = (0, 0 ,0, 255)

    name_text = f"sUPer OFIciAl eYE-D"
    draw.text( (int( 0.3 * width), 40), name_text,text_color ,font = big_font)

    name_text = f"nAmE: {fullRandomName}"
    draw.text( (x + w + 100, y), name_text,text_color ,font = font)

    age_text = f"aGE: {age}"
    draw.text( (x + w + 100, y + 100), age_text,text_color,font = font)

    draw.rectangle((20, 20, width - 20, height - 20), fill = None, outline= (0,0,0), width = 3)

    return background   
    
