import jieba
import logging
jieba.setLogLevel(logging.ERROR)

def tokenize_chinese(text):
    return list(jieba.cut(text, HMM=True))

def tokenize_arabic(text):
    # Fallback: split on space, assuming typical full name order
    return text.strip().split()

def tokenize_korean(text):
    from kiwipiepy import Kiwi
    kiwi = Kiwi()
    tokens = kiwi.tokenize(text)
    return [token.form for token in tokens]

def tokenize_japanese(text):
    import spacy
    nlp = spacy.load("ja_ginza")
    doc = nlp(text)
    return [token.text for token in doc]
