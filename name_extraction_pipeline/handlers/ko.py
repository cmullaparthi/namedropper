from ..tokenizers import tokenize_korean

def get_first_name(name: str):
    tokens = tokenize_korean(name)
    if not tokens:
        return {"first_name": "", "from_model": False, "confidence": 0.0}
    return {"first_name": tokens[-1], "from_model": False, "confidence": 0.6}
