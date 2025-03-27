import unicodedata
from .name_origin_predictor import predict_origin
from .known_given_names import KNOWN_NAMES
from .name_prism_wrapper import infer_name_origin as try_model_infer

COMMON_CULTURE_PATTERNS = {
    "zh": {
        "surnames": {"wang", "li", "zhang", "liu", "chen", "yang", "zhao", "wu", "zhou", "xu", "sun"},
        "script_hint": "CJK UNIFIED"
    },
    "ja": {
        "script_hint": ["HIRAGANA", "KATAKANA"]
    },
    "ko": {
        "script_hint": "HANGUL"
    },
    "vi": {
        "surnames": {"nguyen", "tran", "le", "pham", "hoang", "ngo", "vu", "vo", "dang"}
    },
    "ar": {
        "prefixes": {"al", "bin", "ibn", "abd", "abu"}
    },
    "fr": {
        "prefixes": {"de", "du", "le"}
    },
    "es": {
        "prefixes": {"del", "de", "la"}
    },
    "en": {
        "fallback": True
    }
}

def normalize(name):
    return name.lower().strip().replace(".", "")

def detect_script(text: str):
    for ch in text:
        name = unicodedata.name(ch, "")
        if "CJK UNIFIED" in name:
            return "zh"
        if "HIRAGANA" in name or "KATAKANA" in name:
            return "ja"
        if "HANGUL" in name:
            return "ko"
    return None

def infer_name_language(name: str) -> str:
    lang, conf = predict_origin(name)
    if conf >= 0.7:
        return lang

    script_lang = detect_script(name)
    if script_lang:
        return script_lang

    tokens = [normalize(part) for part in name.split()]
    if not tokens:
        return "xx"

    if tokens[0] in KNOWN_NAMES:
        return KNOWN_NAMES[tokens[0]]

    for lang, rules in COMMON_CULTURE_PATTERNS.items():
        if "surnames" in rules and tokens[0] in rules["surnames"]:
            return lang
        if "prefixes" in rules and tokens[0] in rules["prefixes"]:
            return lang

    return "en"
