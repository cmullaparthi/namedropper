from importlib import import_module
from .name_language_infer import infer_name_language as detect_language
from .handlers import default

SUPPORTED_LANGS = ["en", "fr", "de", "es", "zh", "ja", "ko", "vi", "ar"]

def get_handler(lang):
    try:
        return import_module(f"name_extraction_pipeline.handlers.{lang}").get_first_name
    except ModuleNotFoundError:
        return default.get_first_name

def extract_first_name(full_name: str):
    lang = detect_language(full_name)
    handler = get_handler(lang)
    result = handler(full_name)
    result["language"] = lang
    return result

