import spacy
from spacy.tokens import DocBin
from training_data import TRAINING_DATA
import random
import os


nlp = spacy.load("ro_core_news_md")

# Amestecam datele si le impartim 80% train / 20% validare
random.shuffle(TRAINING_DATA)
split = int(len(TRAINING_DATA) * 0.8)
train_data = TRAINING_DATA[:split]
dev_data = TRAINING_DATA[split:]


def save_data(data, output_path):
    # Salvare training_data in format .spacy
    db = DocBin()
    for text, annot in data:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                print(f"Span invalid: '{text[start:end]}' in: {text}")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


os.makedirs("corpora", exist_ok=True)
save_data(train_data, "corpora/train.spacy")
save_data(dev_data, "corpora/dev.spacy")
print("Fisiere .spacy create cu succes.")
