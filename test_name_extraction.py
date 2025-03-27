import pytest
from name_extraction_pipeline.dispatcher import extract_first_name

test_cases = [
    ("John Smith", "John", "en"),
    ("Jean Dupont", "Jean", "fr"),
    ("Hans Müller", "Hans", "de"),
    ("Carlos Mendez", "Carlos", "es"),
    ("Wang Wei", "Wei", "zh"),
    ("Yamada Taro", "Taro", "ja"),
    ("Kim Min-ji", "Min-ji", "ko"),
    ("Nguyen Thi Minh Khai", "Khai", "vi"),
    ("Dr. Alice Johnson", "Alice", "en"),
    ("Fatima Al Zahra", "Fatima", "xx"),  # fallback for Arabic-like names
]

@pytest.mark.parametrize("full_name,expected_first_name,expected_lang", test_cases)
def test_name_extraction(full_name, expected_first_name, expected_lang):
    result = extract_first_name(full_name)
    assert result["first_name"] == expected_first_name
    assert result["language"] == expected_lang
