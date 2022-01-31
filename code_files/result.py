import os
import cv2
import re
import string
from ocr import text_image
from re_pan_aadhar_match import extract_Aadhaar
from re_pan_aadhar_match import extract_PAN
from names_ner import extract_names

def extract():
    path = "C:/Users/Rachit/Onedrive/Desktop/Files/VS/OCR/duEX6.png"
    text = text_image(path)
    
    names = extract_names(text)
    pan_id = extract_PAN(text)
    aadhaar_id = extract_Aadhaar(text)
    
    print(names,pan_id,aadhaar_id)

if __name__ == '__main__':
    extract()    