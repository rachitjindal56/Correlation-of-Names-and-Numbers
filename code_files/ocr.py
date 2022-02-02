import os
from unittest import result
from PIL import Image
import cv2
import re
import pytesseract
from pytesseract import Output

def text_process(text:str)->str:
    
    # Removing the extra spaces and new line from the 
    # extracted text and converting into upper case
    ocr_text = text.lstrip().rstrip().upper()
    result = re.sub("\n+"," ",ocr_text)
    result = re.sub("\s+"," ",result)
    
    return result

def text_image(path:str)->str:
    
    # Reading images using cv2 module and converting the 
    # extracted image to grayscale for uniformity for 
    # improved text extraction
    image = cv2.imread(path)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    
    # Using Pytesseract for converting image to string
    ocr_text = pytesseract.image_to_string(image,output_type=Output.STRING)
    
    # Text processing
    result = text_process(ocr_text)
    return result