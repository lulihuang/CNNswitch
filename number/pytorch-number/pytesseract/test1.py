# -*- coding: UTF-8 -*-
from PIL import Image
import pytesseract
# 识别中文
#text = pytesseract.image_to_string(Image.open('chinese.png'),lang='chi_sim')
#print text

# 识别english
text = pytesseract.image_to_string(Image.open('7.jpg'))
print(text)


