import os
import cv2
import re
import string
from ocr import text_image
from re_pan_aadhar_match import extract_Aadhaar
from re_pan_aadhar_match import extract_PAN
from names_ner import extract_names
from output_phrasing import final_output

def extract():
    path = "C:/Users/Rachit/Downloads/sample_pan.jpg"
    text = text_image(path)
    
    names = extract_names(text)
    pan_id = extract_PAN(text)
    aadhaar_id = extract_Aadhaar(text)

    sol = final_output(names,pan_id,aadhaar_id)
    
    print(sol)

if __name__ == '__main__':
    # path = input("Enter the path of the image date to be extracted: ")
    # extract(path)
    extract()