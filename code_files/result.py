import os
import cv2
import re
import string
from ocr import text_image
from re_pan_aadhar_match import extract_Aadhaar
from re_pan_aadhar_match import extract_PAN
from names_ner import extract_names
from output_phrasing import final_output

def extract(path:str):

    # Calling the text_image function in ocr file for text extraction
    text = text_image(path)
    
    # Calling the extract_names, extract_PAN and extract_Aadhaar functions 
    # in names_ner and re_pan_aadhar_match files respectively for 
    # data extraction
    names = extract_names(text)
    pan_id = extract_PAN(text)
    aadhaar_id = extract_Aadhaar(text)

    # Calling the final_output function in output_phrasing file for 
    # phrasing output text extracted above
    sol = final_output(names,pan_id,aadhaar_id)
    
    # Printing the the output 
    print(sol)

if __name__ == '__main__':
    path = input("Enter the path of the image date to be extracted: ")
    extract(path)