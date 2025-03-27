import pytest
from name_extraction_pipeline.name_language_infer import infer_name_language
from name_extraction_pipeline.name_origin_predictor import predict_origin

@pytest.mark.parametrize("name,expected_lang", [
    ("Abraham Lincoln", "en"),
    ("Mohammed Al Farsi", "ar"),
    ("Nguyen Van A", "vi"),
    ("Kim Min-Ji", "ko"),
    ("王偉", "zh"),
    ("Fatima Al Zahra", "ar"),
    ("Hans Erik Meyer", "de")
])
def test_infer_name_language(name, expected_lang):
    assert infer_name_language(name) == expected_lang

@pytest.mark.parametrize("name,expected_lang", [
    ("Abraham Lincoln", "en"),
    ("Kim Min-Ji", "ko"),
    ("Fatima Al Zahra", "ar"),
])
def test_predict_origin(name, expected_lang):
    lang, conf = predict_origin(name)
    assert lang == expected_lang
    assert conf >= 0.7
