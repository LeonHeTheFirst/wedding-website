from PIL import Image

img = Image.open('img/logo3.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
        # if item[0] > 150:
        #     newData.append((0, 0, 0, 255))
        # else:
        #     newData.append(item)
        #     print(item)


img.putdata(newData)
img.save("img/logo3_transparent.png", "PNG")