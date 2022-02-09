import inspirobot  # Import the libary
import requests
from bs4 import BeautifulSoup
import os
import lxml
from PIL import Image, ImageFont, ImageDraw 
import textwrap

def photo_downloader(url):
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count =0
    # os.chdir('pictures')
    for i in all_image:
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(f'{count}3d.jpg','wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")

flow = inspirobot.flow()  # Generate a flow object
im_list = []
pdf1_filename = "bbd1.pdf"
for i in range(0, 10):
    for quote in flow:
        print(quote.text, quote.image.url)
        f = open(str(i) + '.jpg','wb')
        f.write(requests.get(quote.image.url).content)
        f.close()
        im = Image.open(str(i) + '.jpg')
        im1 = im.crop((0, 0, 240, 816))
        title_font = ImageFont.truetype('playfair/playfair-font.ttf', 25)
        title_text = textwrap.fill(text=quote.text, width=17)
        image_editable = ImageDraw.Draw(im1)
        image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
        im_list.append(im1)
        im1.save(str(i) + '.jpg')
    flow.new()
    print("-"*50)
im = Image.open("0.jpg")
im.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)

