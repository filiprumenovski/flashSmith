import genanki

def make_basic_model() -> genanki.Model:
    return genanki.Model(
        model_id=998877660,
        name="FlashSmith-Basic",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": "{{Front}}<hr id='answer'>{{Back}}",
            }
        ],
        css="""
.card {
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-size: 20px;
  text-align: left;
  color: black;
  background-color: white;
}
""",
    )

def make_cloze_model() -> genanki.Model:
    return genanki.Model(
        model_id=998877661,
        name="FlashSmith-Cloze",
        fields=[{"name": "Text"}, {"name": "Extra"}],
        templates=[
            {
                "name": "Cloze",
                "qfmt": "{{cloze:Text}}",
                "afmt": "{{cloze:Text}}<br><br>{{Extra}}",
            }
        ],
        css="""
.card {
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-size: 20px;
}
""",
    )
