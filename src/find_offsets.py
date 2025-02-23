import spacy

def print_token_offsets(text):
    """Afișează offset-urile pentru fiecare token din text."""
    nlp = spacy.load("ro_core_news_md")
    doc = nlp(text)
    
    print(f"\nText: {text}")
    print("\nToken-uri și offset-uri:")
    for token in doc:
        print(f"Token: '{token.text}' -> Start: {token.idx}, End: {token.idx + len(token.text)}")

# Texte pentru verificare
texts = [
    "Ce substrat folosesc pentru orhidee",
    "Substratul potrivit pentru orhidee",
    "Cand schimb substratul la ficus",
    "Ce lumina ii trebuie ficusului",
    "Lumina necesara pentru orhidee",
    "Care este programul de udare pentru orhidee",
    "De ce cad frunzele la ficus",
    "Trebuie sa schimb substratul",
    "Am nevoie de un substrat nou",
    "Unde gasesc substrat pentru plante"
]

for text in texts:
    print_token_offsets(text)