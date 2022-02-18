
# Correlation-of-Names-and-Numbers
This project focuses on the extraction of Names, PAN ID and Aadhaar
ID from a scanned document like pdf, images, etc using OCR
(Optical Character Recognition) for extraction of text from images, 
pre-trained Hugging Face NER pipeline model for name extraction and 
regex module for pattern matching of the PAN cards and Aadhaar Card.
The output is a dictionary containing Names and ID's associated with
the given name.

### Project File Structure:
        code_files
        | names_ner.py
        | ocr.py
        | output_phrasing.py
        | re_pan_aadhaar_match.py
        | result.py
        Dataset
        | (Images for testing)
        README.md


## ocr.py

It contains two function: 
#### 1. text_image:
To read and extract the text from images using the 
Pytesseract OCR and Cv2.

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

#### 2. text_process:
To process the extracted text to remove the extra spaces and indentations.

    def text_process(text:str)->str:
        
        # Removing the extra spaces and new line from the 
        # extracted text and converting into upper case

        ocr_text = text.lstrip().rstrip().upper()
        result = re.sub("\n+"," ",ocr_text)
        result = re.sub("\s+"," ",result)
        
        return result

    
## re_pan_aadhaar_match.py

It contains two function:

#### 1. extract_pan:
To extract the matching pattern of the PAN card from image text extracted using text_image function
using the regex module.

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

#### 2. extract_aadhaar:
To extract the matching pattern of the extract_aadhaar card from image text extracted using text_image function
using the regex module.

    def extract_Aadhaar(text:str)->list:
        
        # Defining pattern for Aadhaar Card
        pattern = "\d{4}-\d{4}-\d{4}|\d{4} \d{4} \d{4}"
        
        # Finding the Aadhaar Card numbers using above pattern
        result = re.findall(pattern,text)
        
        if len(result) == 0:
            return []
        
        return result

## names_ner.py

It contains a single function extract_names that takes string as input and
returns the list of the names extracted using a pre-trained Hugging Face NER
model. The model used is "dslim/bert-base-NER-uncased" which is trained on a
rich dataset.

Only the names of the person represented as 'NER' is returned as per the requirement.

    def extract_names(text:str)->list:
        
        # Using a pre-trained Hugging Face model for extracting the names
        # by using the NER pipeline
        
        # Loading the tokenizer
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER-uncased")
        
        # Loading the model
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER-uncased")

        # Defining the NER pipeline with entities as grouped
        nlp = pipeline("ner", model=model, tokenizer=tokenizer,grouped_entities=True)

        # Extracting the names
        ner_results = nlp(text)
        
        names_list = []
        
        # Extracting only the Person name defined as 'PER' by the model
        for obs in ner_results:
            if obs['entity_group'] == 'PER' and len(obs['word']) > 5:
                names_list.append(obs['word'])
        
        return names_list

## output_phrasing.py

This file contains function final_output. 
This function converts the output into the dictionary for the output 
to the result.py file.

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

## result.py

This file compiles functions of all the above files and prints the output in
the dictionary format.

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
## Tech Stack

**Server:** Python, Visual Studio Code, Pytesseract, 
Hugging Face Transformers, Regex


## 🚀 About Me
I'm an ambitious and hardworking pre-final year student, 
with skills in Machine Learning, NLP, Data Science, Analytics, 
and Development.


## 🛠 Skills
Python, C++, Deep Learning, Image Processing, Flask, Heroku,  NLP (Natural Language Processing), Machine Learning, Hugging Face,
Image Processing, OCR(Optical Character Recognition), Regex


## 🔗 Links
[![portfolio](https://img.shields.io/badge/Git-GitHub-blue?style=for-the-badge&logo=appveyor)](https://github.com/rachitjindal56)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rachit-r-jindal-b99a54188/)
[![blog](https://img.shields.io/badge/Blog-Coderspacket-blue?style=for-the-badge&logo=appveyor)](https://coderspacket.com/contributor/rachit99)


## Authors

- [@Rachit R Jindal](https://github.com/rachitjindal56)


## Feedback

If you have any feedback, please reach out at rachitjindal56@gmail.com

