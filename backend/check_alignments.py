import spacy
from spacy.training import offsets_to_biluo_tags
from spacy.tokens import Doc
from training_data import TRAINING_DATA

def check_alignments():
    
    nlp = spacy.load("ro_core_news_md")
    
    print("Verificare alinieri pentru datele de antrenare:\n")
    
    for text, annotations in TRAINING_DATA:
        doc = nlp.make_doc(text)
        tags = offsets_to_biluo_tags(doc, annotations.get("entities"))
        
        tokens = [t.text for t in doc]
        print(f"\nText: {text}")
        print("Tokens:", tokens)
        print("Tags:", tags)
        print("Entități definite:", annotations.get("entities"))
        
        if '-' in tags:
            print("⚠️ AVERTISMENT: Aliniere incorectă detectată!")
            
        print("-" * 50)

if __name__ == "__main__":
    check_alignments()