import spacy
from spacy.tokens import DocBin
from training_data import TRAINING_DATA
import random
import os

# Încarcă modelul de bază (poți folosi și "ro_core_news_sm")
nlp = spacy.load("ro_core_news_md")

# Amestecăm datele și le împărțim 80% train / 20% dev
random.shuffle(TRAINING_DATA)
split = int(len(TRAINING_DATA) * 0.8)
train_data = TRAINING_DATA[:split]
dev_data = TRAINING_DATA[split:]

# Funcție de salvare în format .spacy


def save_data(data, output_path):
    db = DocBin()
    for text, annot in data:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                print(f"⚠️ Span invalid: '{text[start:end]}' în: {text}")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


# Creăm folderul dacă nu există
os.makedirs("corpora", exist_ok=True)
save_data(train_data, "corpora/train.spacy")
save_data(dev_data, "corpora/dev.spacy")
print("✅ Fișiere .spacy create cu succes.")
