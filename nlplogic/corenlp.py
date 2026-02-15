from textblob import TextBlob
import wikipedia

def search(name):
    print(f"Searching for {{name}}")
    return wikipedia.search(name)

def summary(name):
    print(f"Summarize for {name}")
    return wikipedia.summary(name)

def get_textblob(text):
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    text = summary(name)
    blob = get_textblob(text)
    phrases = blob.noun_phrases    
    return phrases
