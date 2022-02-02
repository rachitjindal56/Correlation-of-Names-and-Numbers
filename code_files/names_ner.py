from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

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