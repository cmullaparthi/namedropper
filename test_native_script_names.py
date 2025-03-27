import pytest
from name_extraction_pipeline.dispatcher import extract_first_name

native_script_cases = [
    ("王偉", "偉", "zh", 0.8),
    ("山田太郎", "太郎", "ja", 0.6),
    ("김민지", "민지", "ko", 0.6),
    ("فاطمة الزهراء", "فاطمة", "ar", 0.5),
    ("张伟", "伟", "zh", 0.8),
    ("이수민", "수민", "ko", 0.6),
    ("佐藤健", "健", "ja", 0.6),
]

@pytest.mark.parametrize("full_name,expected_first,expected_lang,min_conf", native_script_cases)
def test_native_script_names(full_name, expected_first, expected_lang, min_conf):
    result = extract_first_name(full_name)
    assert result["first_name"] == expected_first
    assert result["language"] == expected_lang
    assert result["confidence"] >= min_conf
