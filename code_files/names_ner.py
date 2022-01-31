from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def extract_names(text:str)->list:
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(text)
    return ner_results