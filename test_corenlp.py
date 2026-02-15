from nlplogic.corenlp import get_phrases

def test_get_phrases():
    assert "vietnam" in get_phrases("vietnam")