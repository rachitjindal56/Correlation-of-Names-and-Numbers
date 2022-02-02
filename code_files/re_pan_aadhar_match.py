import re

def extract_PAN(text:str)->list:
    
    # Defining pattern for PAN Card
    pattern = "[A-Z]{3}[ABCFGHLJPTF][A-Z][0-9]{4}[A-Z]"
    
    # Converting the text to upper case
    text = text.upper()
    
    # Finding the PAN Card ID using above pattern
    result = re.findall(pattern,text)
    
    # If the pattern is not found an empty list is returned
    if len(result) == 0:
        return []

    return result

def extract_Aadhaar(text:str)->list:
    
    # Defining pattern for Aadhaar Card
    pattern = "\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4}"
    
    # Finding the Aadhaar Card numbers using above pattern
    result = re.findall(pattern,text)
    
    # If the pattern is not found an empty list is returned
    if len(result) == 0:
        return []
    
    return result