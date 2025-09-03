````markdown
# FlashSmith

FlashSmith is my first useful Python project — a learning milestone in my programming journey.  
This tool converts CSV files into Anki `.apkg` decks.

---

## About this Project
This project started as a **proof of concept**: could I engineer a working system that takes structured data and produces a functional output?  

- The **code scaffolding** was built with AI assistance (ChatGPT).  
- The **design choices, refactor into modules, and engineering flow** were my focus.  
- My goal is to show I can structure, run, and maintain a Python package — even at the very start of my coding journey.  

This repo represents:
- ✅ My first end-to-end working script.  
- ✅ My introduction to Python packaging and modular code.  
- ✅ A foundation I plan to extend and improve.  

---

## Requirements
- Python 3.10+  
- Install dependencies (one-time setup):
  ```bash
  pip install -r requirements.txt
````

---

## Usage

1. Put your source CSVs in the `examples/` folder.

   * Each row = one flashcard.
   * Header must be:

     ```
     Deck,Subdeck,Type,Front,Back
     ```

2. Build a deck:

   ```bash
   python3 -m flashsmith.flashsmith examples/aminoacids.csv --out dist
   ```

3. Import the generated `.apkg` file from the `dist/` folder into Anki.

---

## Example

```bash
python3 -m flashsmith.flashsmith examples/calculus.csv --out dist
```

Output:

```
[flashsmith] built deck: dist/Calculus I.apkg
  - Derivatives: 2 cards
```

---

## Folder Structure

```
flashsmith/
├── flashsmith/          # main package
│   ├── __init__.py      # marks this as a Python package
│   ├── flashsmith.py    # CLI entry point
│   ├── builder.py       # deck building logic
│   ├── validator.py     # CSV validation
│   ├── models.py        # Anki card models
│   └── utils.py         # helpers (stable_guid, etc.)
├── examples/            # sample CSVs
├── dist/                # generated Anki decks (.apkg)
├── media/               # optional images/audio
├── tests/               # unit tests (future)
├── requirements.txt
└── pyproject.toml
```

---

## Quickstart

From a fresh clone of the repo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m flashsmith.flashsmith examples/calculus.csv --out dist
```

Then import the `.apkg` from `dist/` into Anki.

---

## Future Directions

* Add support for images and audio in flashcards.
* Extend validation rules for CSV input.
* Explore richer card templates beyond basic and cloze.
* Write unit tests in `tests/` for validation and building.

---

## Reflection

This project is **not about perfect original code** — it’s about learning how to think like an engineer:

* how to structure a repo,
* how to separate concerns into modules,
* how to run and test software in a reproducible way.

It’s the first step in what will be a growing portfolio of Python and Data Science projects.

```
```
