from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint as r

def mask(logo, back, blur=0):
    im1 = Image.open(back)
    im2 = Image.open(logo)

    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((0, 0, 250, 250), fill=255)

    im1 = im1.filter(ImageFilter.BoxBlur(blur))
    im1.paste(im2, (45, 25), mask_im)
    print(im1)
    return im1

def create(logo, back, name, desc, phone, addr, font, text_size, text_color, blur=0):
    im1 = Image.open(back)
    im2 = Image.open(logo)

    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((0, 0, 250, 250), fill=255)

    im1 = im1.filter(ImageFilter.BoxBlur(blur))
    im1.paste(im2, (45, 25), mask_im)

    head = ImageFont.truetype(font, text_size + 10)
    font = ImageFont.truetype(font, text_size)
    drawer = ImageDraw.Draw(im1)

    drawer.text((80, 300), name, font=head, fill=text_color)
    drawer.text((80, 350), desc, font=font, fill=text_color)
    drawer.text((80, 430), phone, font=font, fill=text_color)
    drawer.text((80, 500), addr, font=font, fill=text_color)

    url = f"card_photo/{name.split('.')[0]} _ {r(0, 100000)}.jpg"
    im1.save(f"card/res/{url}", quality=95)
    return url
