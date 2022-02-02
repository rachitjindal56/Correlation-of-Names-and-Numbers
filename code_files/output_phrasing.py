import re 
import string

def final_output(names:list,pan_id:list,aadhar_id:list)->list:
    sol = []
    
    # If the Aadhaar ID and PAN ID are empty then returning the list
    # with NO ID's
    if len(pan_id) == 0 and len(aadhar_id) == 0:
        sol.append("No ID found")
        
    # If the Aadhaar ID is empty then returning the list
    # with Names and PAN ID
    elif len(aadhar_id) == 0:
        for name,pan in zip(names,pan_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = pan
            zipped["Aadhar"] = ""
            
            sol.append(zipped)
    
    # If the PAN ID is empty then returning the list
    # with Names and Aadhaar ID
    elif len(pan_id) == 0:
        for name,adh in zip(names,aadhar_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = ""
            zipped["Aadhar"] = adh
            
            sol.append(zipped)
    
    # If the Aadhaar ID and PAN ID are not empty then returning the list
    # with Names, PAN and Aadhaar ID's
    else:
        for name,pan in zip(names,pan_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = pan
            zipped["Aadhar"] = ""
            
            sol.append(zipped)
            
    return sol