from typing import List, Tuple
import sys
import spacy


class ModelTester:
    def __init__(self, model_dir: str):
        try:
            self.nlp = spacy.load(model_dir)
            print(f"Model incarcat cu succes din {model_dir}")
        except OSError as e:
            print(f"Eroare la incarcarea modelului: {e}")
            sys.exit(1)

    def test_single_query(self, text: str) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def run_test_suite(self, local_test_cases: List[str]) -> None:
        print("\nRulare teste model NER:")
        print("-" * 50)

        for i, text in enumerate(local_test_cases, 1):
            print(f"\nTest {i}/{len(local_test_cases)}")
            print(f"Text: {text}")
            entities = self.test_single_query(text)

            if entities:
                print("Entitati gasite:")
                for ent_text, ent_label in entities:
                    print(f" - '{ent_text}' -> {ent_label}")
            else:
                print("Nu s-au gasit entitati.")

            print("-" * 30)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        "Cum ud orhideea mea?",
        "Ficusul are frunze galbene",
        "Care este substratul potrivit pentru orhidee?",
        "De ce cad frunzele la ficus?",
        "Nu stiu ce sa fac cu planta mea",
        "Orhideea are radacini putrede",
        "Cat de multa lumina ii trebuie ficusului?",
        "Cand trebuie sa schimb substratul la orhidee?",
        "Am probleme cu caderea frunzelor la ficus",
        "Ficusului ii cad frunzele",
        "Orhideea are nevoie de lumina",
        "Substratul pentru orhidee trebuie schimbat",
        "De ce are orhideea frunze galbene?",
        "Ficusul nu creste bine in lumina directa",
        "Trebuie sa ud orhideea in fiecare zi?"
    ]

    try:
        tester = ModelTester("./model")
        tester.run_test_suite(test_cases)

    except KeyboardInterrupt:
        print("\nTestare intrerupta de utilizator.")
    except OSError as e:
        print(f"\nEroare in timpul testarii: {e}")
