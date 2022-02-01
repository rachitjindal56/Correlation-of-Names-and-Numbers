import os
import cv2
import re
import string
from ocr import text_image
from re_pan_aadhar_match import extract_Aadhaar
from re_pan_aadhar_match import extract_PAN
from names_ner import extract_names

def extract(path:str):
    path = "C:/Users/Rachit/Onedrive/Desktop/Files/VS/OCR/duEX6.png"
    text = text_image(path)
    
    
    names = extract_names(text)
    pan_id = extract_PAN(text)
    aadhaar_id = extract_Aadhaar(text)

    sol = []
    
    for name,pan,adh in zip(names,pan_id,aadhaar_id):
        zipped = {}
        zipped["Name"] = name
        zipped["PAN"] = pan
        zipped["Aadhar"] = adh
        
        sol.append(zipped)
        
    print(sol)

if __name__ == '__main__':
    path = input("Enter the path of the image date to be extracted: ")
    extract(path)