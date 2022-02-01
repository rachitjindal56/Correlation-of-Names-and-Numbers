from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def extract_names(text:str)->list:
    # tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    # model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    # nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    nlp = pipeline("ner", grouped_entities=True)

    ner_results = nlp(text)
    
    if len(ner_results) == 0:
        return []
    
    names_list = []
    
    for obs in ner_results:
        if obs['entity_group'] == 'PER':
            names_list.append(obs['word'])
    
    return names_list