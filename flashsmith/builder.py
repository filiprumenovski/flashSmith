import genanki
from pathlib import Path
from .models import make_basic_model, make_cloze_model
from .utils import stable_guid

def build_package_grouped(rows, out_dir: str, dry_run: bool = False):
    decks = {}

    for row in rows:
        deck_name = row["Deck"]
        subdeck = row["Subdeck"]
        note_type = row["Type"]
        front = row["Front"]
        back = row["Back"]

        deck_id = stable_guid(deck_name, subdeck)
        deck_key = f"{deck_name}::{subdeck}"
        if deck_key not in decks:
            decks[deck_key] = genanki.Deck(deck_id, deck_key)

        if note_type.lower() == "basic":
            model = make_basic_model()
            note = genanki.Note(model=model, fields=[front, back])
        elif note_type.lower() == "cloze":
            model = make_cloze_model()
            note = genanki.Note(model=model, fields=[front, back])
        else:
            raise ValueError(f"Unknown note type: {note_type}")

        decks[deck_key].add_note(note)

    Path(out_dir).mkdir(parents=True, exist_ok=True)

    for deck_key, deck in decks.items():
        pkg = genanki.Package(deck)
        out_path = Path(out_dir) / f"{deck_key.split('::')[0]}.apkg"
        if not dry_run:
            pkg.write_to_file(str(out_path))
        print(f"[flashsmith] built deck: {out_path}")
        print(f"  - {deck_key}: {len(deck.notes)} cards")
