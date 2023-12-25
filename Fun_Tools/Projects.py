from PIL import Image
import face_recognition
import random
import os


image = face_recognition.load_image_file(_imgUrl)
face_locations = face_recognition.face_locations(image)

n = 1

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"/Users/Yoyo/file/{n}.png")
    n = n + 1
    
files = os.listdir("/Users/Yoyo/file")
lucky = random.choice(files)
lucky_dir = os.path.join("/Users/Yoyo/file",lucky)  
background = Image.open('/Users/Yoyo/back.png')
verse = Image.open(lucky_dir)


def mix(img1,img2,coordinator):
    img1 = img1.resize((2000,2000))
    img2 = img2.resize((1000,1200))
    img1.paste(img2, coordinator)
    return img1

co = (500, 350)
background = mix(background, verse, co)
background.save("/Users/Yoyo/success.png")