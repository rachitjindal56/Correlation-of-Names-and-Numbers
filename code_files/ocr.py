import os
from PIL import Image
import cv2
import re
import pytesseract
from pytesseract import Output

def text_image(path:str)->str:
    
    image = cv2.imread(path)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    
    ocr_text = pytesseract.image_to_string(image,output_type=Output.STRING)
    
    result = re.sub("\n+"," ",ocr_text).upper()
    return result