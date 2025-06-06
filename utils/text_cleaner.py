import spacy
import string

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())  # Lowercase and parse with spaCy
    tokens = []

    for token in doc:
        if (
            token.text not in string.punctuation and
            not token.is_stop and
            token.is_alpha
        ):
            tokens.append(token.lemma_)  # Append lemmatized word

    return " ".join(tokens)
