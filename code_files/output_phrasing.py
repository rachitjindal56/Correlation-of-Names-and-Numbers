import re 
import string

def final_output(names:list,pan_id:list,aadhar_id:list)->list:
    sol = []
    
    if len(aadhar_id) == 0:
        for name,pan in zip(names,pan_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = pan
            zipped["Aadhar"] = ""
            
            sol.append(zipped)
    
    elif len(pan_id) == 0:
        for name,adh in zip(names,aadhar_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = ""
            zipped["Aadhar"] = adh
            
            sol.append(zipped)
    
    elif len(pan_id) == 0 and len(aadhar_id) == 0:
        sol.append("No ID found")
        
    else:
        for name,pan in zip(names,pan_id):
            zipped = {}
            zipped["Name"] = name
            zipped["PAN"] = pan
            zipped["Aadhar"] = ""
            
            sol.append(zipped)
            
    return sol