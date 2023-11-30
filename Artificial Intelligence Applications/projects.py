import os
allImgPath = '/yequ/photo'
imglist = os.listdir(allImgPath)

from aip import AipImageClassify
APP_ID = '10254521'
API_KEY = 'KJe5566sh11GEjIAdThdY'
SECRET_KEY = 'KwkzHe5566USH1ZhEnM1OUHss'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

for imgname in imglist:
    if imgname[0] == '.' or '.' not in imgname:
        continue
    filePath = allImgPath + '/' + imgname
    with open(filePath, 'rb') as file:
        image = file.read()
    ending = client.advancedGeneral(image)
    if "result" in ending:
        value = ending['result'][0].get('root', '未分类')
        label = value.split("-")[0]
        targetPath = allImgPath + '/' + label
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        import shutil
        newPath = shutil.move(filePath, targetPath)
        print(f"已经移动到：{newPath}") # Mean "Alreay move to {path}"

from aip import AipFace
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

import base64
def renlian(file):
    res = file.read()
    img = base64.b64encode(res)
    img = str(img, 'utf-8')
    options = {
        'max_face_num' : 10,
        'face_field': 'quality,mask',
    }
    img_type = "BASE64"
    ret_data = client.detect(img, img_type, options)
    return ret_data

personPath = "/yequ/photo/人物"
personlist = os.listdir(personPath)
for person in personlist:
    if person[0] == '.' or '.' not in person:
        continue
    person_path = personPath + "/" + person
    with open(person_path, "rb") as file:
        ret_data = renlian(file)
        from PIL import Image      
        from PIL import ImageDraw
        with Image.open(person_path) as img:
            draw_img = ImageDraw.Draw(img)
            if ret_data['error_msg'] == 'SUCCESS':
                for face_msg in ret_data['result']['face_list']:
                    location = face_msg['location']
                    x1 = location['left']
                    y1 = location['top']
                    x2 = x1 + location['width']
                    y2 = y1 + location['height']
                    from PIL import ImageFont
                    font_path = '/yequ/STHeiti-Medium-4.ttc'
                    font_size = location['width'] // 5
                    font = ImageFont.truetype(font_path, font_size)
                    mask = face_msg['mask']
                    if mask["type"] == 1:
                        color = 'lightgreen'
                        text = '已佩戴口罩' # Mean "Mask wear"
                    else:
                        color = 'red'
                        text = '未佩戴口罩' # Mean "Mask not wear"
                    draw_img.rectangle([x1, y1, x2, y2], outline=color, width=2)
                    draw_img.rectangle([x1, y2, x2, y2 + font_size * 2], fill=color)
                    draw_img.text([x1, y2], text, 'white', font)
            img.save("/yequ/photo/口罩/"+person)
