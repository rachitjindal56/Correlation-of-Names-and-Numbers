import re

def extract_PAN(text:str)->list:
    pattern = "[A-Z]{3}[ABCFGHLJPTF][A-Z][0-9]{4}[A-Z]"
    
    text = text.upper()
    result = re.findall(pattern,text)
    
    if len(result) == 0:
        return []

    return result

def extract_Aadhaar(text:str)->list:
    pattern = "\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4}"
    
    result = re.findall(pattern,text)
    
    if len(result) == 0:
        return []
    
    return result