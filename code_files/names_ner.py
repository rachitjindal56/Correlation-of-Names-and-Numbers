from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def extract_names(text:str)->list:
    
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER-uncased")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER-uncased")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer,grouped_entities=True)
    # nlp = pipeline("ner", grouped_entities=True)

    ner_results = nlp(text)
    
    names_list = []
    
    for obs in ner_results:
        if obs['entity_group'] == 'PER' and len(obs['word']) > 5:
            names_list.append(obs['word'])
    
    return names_list