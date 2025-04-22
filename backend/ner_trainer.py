import spacy
from spacy.tokens import Doc
from spacy.training import Example
from training_data import TRAINING_DATA
import random
import os
import shutil


def train_ner(model_name: str = "ro_core_news_md", output_dir: str = "model", n_iter: int = 60):

    print("Initializare antrenare...")

    if os.path.exists(output_dir):
        print(f"Stergem modelul vechi din {output_dir}")
        shutil.rmtree(output_dir)

    os.makedirs(output_dir)

    nlp = spacy.load(model_name)
    print(f"Modelul incarcat: {model_name}")

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    for _, annotations in TRAINING_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    print("\nIncepem antrenarea...")
    with nlp.disable_pipes(*other_pipes):

        optimizer = nlp.begin_training()
        examples = []
        for text, annots in TRAINING_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annots)
            examples.append(example)

        best_loss = float('inf')
        patience = 10
        no_improvement = 0
        min_loss_threshold = 1.0  # loss minim pentru early stopping
        improvement_threshold = 0.01  # minimul pentru imbunatatire

        # Antrenare
        for itn in range(n_iter):
            random.shuffle(examples)
            losses = {}
            nlp.update(examples, drop=0.2, sgd=optimizer, losses=losses)
            current_loss = losses['ner']

            print(f"Iteration {itn + 1}, Loss: {current_loss:.6f}")

            if current_loss < best_loss - improvement_threshold:
                best_loss = current_loss
                no_improvement = 0
            else:
                no_improvement += 1

            # Early stopping
            if current_loss < min_loss_threshold and no_improvement >= patience:
                print(
                    f"\nEarly stopping la iteratia {itn + 1} - Nu s-au mai observat imbunatatiri semnificative")
                print(f"Cel mai bun loss: {best_loss:.6f}")
                break

            if current_loss < 0.1:
                print(
                    f"\nAntrenare oprita la iteratia {itn + 1} - Loss-ul e suficient de mic")
                break

    nlp.to_disk(output_dir)
    print(f"\nModel salvat in {output_dir}")


if __name__ == "__main__":
    print("Starting training process...")
    train_ner()
    print("Training finished!")
