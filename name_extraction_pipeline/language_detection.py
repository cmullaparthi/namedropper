from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import unicodedata

DetectorFactory.seed = 42

SUPPORTED_LANGS = {"en", "fr", "de", "es", "zh", "ja", "ko", "vi"}

def detect_language(name: str) -> str:
    try:
        # Use script-based detection for short inputs
        if len(name.split()) < 3:
            return detect_by_script(name)
        lang = detect(name)
        return lang if lang in SUPPORTED_LANGS else "xx"
    except LangDetectException:
        return detect_by_script(name)

def detect_by_script(text: str) -> str:
    for ch in text:
        name = unicodedata.name(ch, "")
        if "CJK UNIFIED" in name:
            return "zh"
        if "HIRAGANA" in name or "KATAKANA" in name:
            return "ja"
        if "HANGUL" in name:
            return "ko"
    return "xx"
