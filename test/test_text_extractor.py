from src.text_extractor import text_extractor
import pytest

@pytest.mark.text_extractor
def test_funciona():         
    assert text_extractor('./test/test_string.txt') == ["a","b","c","d","e","f","g","h","i","j"]

def test_doc_vacio():
    assert text_extractor('./test/vacio.txt') == []
