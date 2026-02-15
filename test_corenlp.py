from nlplogic.corenlp import search, summary, get_textblob, get_phrases

def test_get_phrases():
    assert "vietnam" in get_phrases("vietnam")