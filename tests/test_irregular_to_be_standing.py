from exprimidora import IrregularToBeStanding

def test_participle_and_gerund():
    verb = IrregularToBeStanding()
    assert verb.gerund() == "estando"
    assert verb.participle() == "estado"

def test_indicative_present():
    verb = IrregularToBeStanding()
    assert verb.indicative_present("yo") == "estoy"
    assert verb.indicative_present() == {
        "yo": "estoy",
        "tú": "estás",
        "vos": "estás",
        "usted": "está",
        "él": "está",
        "ella": "está",
        "nosotros": "estamos",
        "nosotras": "estamos",
        "vosotros": "estais",
        "vosotras": "estais",
        "ustedes": "están",
        "ellos": "están",
        "ellas": "están",
    }

def test_indicative_imperfect():
    verb = IrregularToBeStanding()
    assert verb.indicative_imperfect("yo") == "estaba"
    assert verb.indicative_imperfect() == {
        "yo": "estaba",
        "tú": "estabas",
        "vos": "estabas",
        "usted": "estaba",
        "él": "estaba",
        "ella": "estaba",
        "nosotros": "estábamos",
        "nosotras": "estábamos",
        "vosotros": "estábais",
        "vosotras": "estábais",
        "ustedes": "estaban",
        "ellos": "estaban",
        "ellas": "estaban",
    }

def test_indicative_preterite():
    verb = IrregularToBeStanding()
    assert verb.indicative_preterite("yo") == "estuve"
    assert verb.indicative_preterite() == {
        "yo": "estuve",
        "tú": "estuviste",
        "vos": "estuviste",
        "usted": "estuvo",
        "él": "estuvo",
        "ella": "estuvo",
        "nosotros": "estuvimos",
        "nosotras": "estuvimos",
        "vosotros": "estuvisteis",
        "vosotras": "estuvisteis",
        "ustedes": "estuvieron",
        "ellos": "estuvieron",
        "ellas": "estuvieron",
    }

def test_indicative_future():
    verb = IrregularToBeStanding()
    assert verb.indicative_future("yo") == "estaré"
    assert verb.indicative_future() == {
        "yo": "estaré",
        "tú": "estarás",
        "vos": "estarás",
        "usted": "estará",
        "él": "estará",
        "ella": "estará",
        "nosotros": "estaremos",
        "nosotras": "estaremos",
        "vosotros": "estaréis",
        "vosotras": "estaréis",
        "ustedes": "estarán",
        "ellos": "estarán",
        "ellas": "estarán",
    }

def test_indicative_conditional():
    verb = IrregularToBeStanding()
    assert verb.indicative_conditional("yo") == "estaría"
    assert verb.indicative_conditional() == {
        "yo": "estaría",
        "tú": "estarías",
        "vos": "estarías",
        "usted": "estaría",
        "él": "estaría",
        "ella": "estaría",
        "nosotros": "estaríamos",
        "nosotras": "estaríamos",
        "vosotros": "estaríais",
        "vosotras": "estaríais",
        "ustedes": "estarían",
        "ellos": "estarían",
        "ellas": "estarían",
    }

def test_indicative_present_perfect():
    verb = IrregularToBeStanding()
    assert verb.indicative_present_perfect("yo") == "he estado"
    assert verb.indicative_present_perfect() == {
        "yo": "he estado",
        "tú": "has estado",
        "vos": "has estado",
        "usted": "ha estado",
        "él": "ha estado",
        "ella": "ha estado",
        "nosotros": "hemos estado",
        "nosotras": "hemos estado",
        "vosotros": "habéis estado",
        "vosotras": "habéis estado",
        "ustedes": "han estado",
        "ellos": "han estado",
        "ellas": "han estado",
    }

def test_indicative_past_perfect():
    verb = IrregularToBeStanding()
    assert verb.indicative_past_perfect("yo") == "había estado"
    assert verb.indicative_past_perfect() == {
        "yo": "había estado",
        "tú": "habías estado",
        "vos": "habías estado",
        "usted": "había estado",
        "él": "había estado",
        "ella": "había estado",
        "nosotros": "habíamos estado",
        "nosotras": "habíamos estado",
        "vosotros": "habíais estado",
        "vosotras": "habíais estado",
        "ustedes": "habían estado",
        "ellos": "habían estado",
        "ellas": "habían estado",
    }

def test_indicative_past_anterior():
    verb = IrregularToBeStanding()
    assert verb.indicative_past_anterior("yo") == "hube estado"
    assert verb.indicative_past_anterior() == {
        "yo": "hube estado",
        "tú": "hubiste estado",
        "vos": "hubiste estado",
        "usted": "hubo estado",
        "él": "hubo estado",
        "ella": "hubo estado",
        "nosotros": "hubimos estado",
        "nosotras": "hubimos estado",
        "vosotros": "hubisteis estado",
        "vosotras": "hubisteis estado",
        "ustedes": "hubieron estado",
        "ellos": "hubieron estado",
        "ellas": "hubieron estado",
    }

def test_indicative_future_perfect():
    verb = IrregularToBeStanding()
    assert verb.indicative_future_perfect("yo") == "habré estado"
    assert verb.indicative_future_perfect() == {
        "yo": "habré estado",
        "tú": "habrás estado",
        "vos": "habrás estado",
        "usted": "habrá estado",
        "él": "habrá estado",
        "ella": "habrá estado",
        "nosotros": "habremos estado",
        "nosotras": "habremos estado",
        "vosotros": "habréis estado",
        "vosotras": "habréis estado",
        "ustedes": "habrán estado",
        "ellos": "habrán estado",
        "ellas": "habrán estado",
    }

def test_indicative_conditional_perfect():
    verb = IrregularToBeStanding()
    assert verb.indicative_conditional_perfect("yo") == "habría estado"
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría estado",
        "tú": "habrías estado",
        "vos": "habrías estado",
        "usted": "habría estado",
        "él": "habría estado",
        "ella": "habría estado",
        "nosotros": "habríamos estado",
        "nosotras": "habríamos estado",
        "vosotros": "habríais estado",
        "vosotras": "habríais estado",
        "ustedes": "habrían estado",
        "ellos": "habrían estado",
        "ellas": "habrían estado",
    }

def test_subjunctive_present():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_present("yo") == "esté"
    assert verb.subjunctive_present() == {
        "yo": "esté",
        "tú": "estés",
        "vos": "estés",
        "usted": "esté",
        "él": "esté",
        "ella": "esté",
        "nosotros": "estemos",
        "nosotras": "estemos",
        "vosotros": "estemos",
        "vosotras": "estéis",
        "ustedes": "estéis",
        "ellos": "estén",
        "ellas": "estén",
    }

def test_subjunctive_imperfect_preterite():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_imperfect_preterite("yo") == "estuviera"
    assert verb.subjunctive_imperfect_preterite() == {
        "yo": "estuviera",
        "tú": "estuvieras",
        "vos": "estuvieras",
        "usted": "estuviera",
        "él": "estuviera",
        "ella": "estuviera",
        "nosotros": "estuviéramos",
        "nosotras": "estuviéramos",
        "vosotros": "estuvierais",
        "vosotras": "estuvierais",
        "ustedes": "estuvieran",
        "ellos": "estuvieran",
        "ellas": "estuvieran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_imperfect_preterite_alternate("yo") == "estuviese"
    assert verb.subjunctive_imperfect_preterite_alternate() == {
        "yo": "estuviese",
        "tú": "estuvieses",
        "vos": "estuvieses",
        "usted": "estuviese",
        "él": "estuviese",
        "ella": "estuviese",
        "nosotros": "estuviésemos",
        "nosotras": "estuviésemos",
        "vosotros": "estuvieseis",
        "vosotras": "estuvieseis",
        "ustedes": "estuviesen",
        "ellos": "estuviesen",
        "ellas": "estuviesen",
    }

def test_subjunctive_future():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_future("yo") == "estuviere"
    assert verb.subjunctive_future() == {
        "yo": "estuviere",
        "tú": "estuvieres",
        "vos": "estuvieres",
        "usted": "estuviere",
        "él": "estuviere",
        "ella": "estuviere",
        "nosotros": "estuviéremos",
        "nosotras": "estuviéremos",
        "vosotros": "estuviereis",
        "vosotras": "estuviereis",
        "ustedes": "estuvieren",
        "ellos": "estuvieren",
        "ellas": "estuvieren",
    }

def test_subjunctive_present_perfect():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_present_perfect("yo") == "haya estado"
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya estado",
        "tú": "hayas estado",
        "vos": "hayas estado",
        "usted": "haya estado",
        "él": "haya estado",
        "ella": "haya estado",
        "nosotros": "hayamos estado",
        "nosotras": "hayamos estado",
        "vosotros": "hayáis estado",
        "vosotras": "hayáis estado",
        "ustedes": "hayan estado",
        "ellos": "hayan estado",
        "ellas": "hayan estado",
    }

def test_subjunctive_past_perfect():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_past_perfect("yo") == "hubiera estado"
    assert verb.subjunctive_past_perfect() == {
        "yo": "hubiera estado",
        "tú": "hubieras estado",
        "vos": "hubieras estado",
        "usted": "hubiera estado",
        "él": "hubiera estado",
        "ella": "hubiera estado",
        "nosotros": "hubiéramos estado",
        "nosotras": "hubiéramos estado",
        "vosotros": "hubierais estado",
        "vosotras": "hubierais estado",
        "ustedes": "hubieran estado",
        "ellos": "hubieran estado",
        "ellas": "hubieran estado",
    }

def test_subjunctive_past_perfect_alternate():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_past_perfect_alternate("yo") == "hubiese estado"
    assert verb.subjunctive_past_perfect_alternate() == {
        "yo": "hubiese estado",
        "tú": "hubieses estado",
        "vos": "hubieses estado",
        "usted": "hubiese estado",
        "él": "hubiese estado",
        "ella": "hubiese estado",
        "nosotros": "hubiésemos estado",
        "nosotras": "hubiésemos estado",
        "vosotros": "hubieseis estado",
        "vosotras": "hubieseis estado",
        "ustedes": "hubiesen estado",
        "ellos": "hubiesen estado",
        "ellas": "hubiesen estado",
    }

def test_subjunctive_future_perfect():
    verb = IrregularToBeStanding()
    assert verb.subjunctive_future_perfect("yo") == "hubiere estado"
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere estado",
        "tú": "hubieres estado",
        "vos": "hubieres estado",
        "usted": "hubiere estado",
        "él": "hubiere estado",
        "ella": "hubiere estado",
        "nosotros": "hubiéremos estado",
        "nosotras": "hubiéremos estado",
        "vosotros": "hubiereis estado",
        "vosotras": "hubiereis estado",
        "ustedes": "hubieren estado",
        "ellos": "hubieren estado",
        "ellas": "hubieren estado",
    }

def test_imperative_affirmative():
    verb = IrregularToBeStanding()
    assert verb.imperative_affirmative("tú") == "está"
    assert verb.imperative_affirmative() == {
        "tú": "está",
        "vos": "está",
        "usted": "esté",
        "nosotros": "estemos",
        "nosotras": "estemos",
        "vosotros": "estad",
        "vosotras": "estad",
        "ustedes": "estén",
    }

def test_imperative_negative():
    verb = IrregularToBeStanding()
    assert verb.imperative_negative("tú") == "estés"
    assert verb.imperative_negative() == {
        "tú": "estés",
        "vos": "estés",
        "usted": "esté",
        "nosotros": "estemos",
        "nosotras": "estemos",
        "vosotros": "estéis",
        "vosotras": "estéis",
        "ustedes": "estén",
    }
