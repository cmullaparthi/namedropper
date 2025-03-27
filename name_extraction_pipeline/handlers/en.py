import spacy
nlp = spacy.load("en_core_web_sm")

def get_first_name(name: str):
    doc = nlp(name)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return {"first_name": ent.text.split()[0], "from_model": True}
    from .. import fallback
    return fallback.get_first_name(name)
