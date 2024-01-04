from exprimidora import IrregularToBeExisting

def test_participle_and_gerund():
    verb = IrregularToBeExisting()
    assert verb.gerund() == "siendo"
    assert verb.participle() == "sido"

def test_indicative_present():
    verb = IrregularToBeExisting()
    assert verb.indicative_present("yo") == "soy"
    assert verb.indicative_present() == {
        "yo": "soy",
        "tú": "eres",
        "vos": "sos",
        "usted": "es",
        "él": "es",
        "ella": "es",
        "nosotros": "somos",
        "nosotras": "somos",
        "vosotros": "sois",
        "vosotras": "sois",
        "ustedes": "son",
        "ellos": "son",
        "ellas": "son",
    }

def test_indicative_imperfect():
    verb = IrregularToBeExisting()
    assert verb.indicative_imperfect("yo") == "era"
    assert verb.indicative_imperfect() == {
        "yo": "era",
        "tú": "eras",
        "vos": "eras",
        "usted": "era",
        "él": "era",
        "ella": "era",
        "nosotros": "éramos",
        "nosotras": "éramos",
        "vosotros": "erais",
        "vosotras": "erais",
        "ustedes": "eran",
        "ellos": "eran",
        "ellas": "eran",
    }

def test_indicative_preterite():
    verb = IrregularToBeExisting()
    assert verb.indicative_preterite("yo") == "fui"
    assert verb.indicative_preterite() == {
        "yo": "fui",
        "tú": "fuiste",
        "vos": "fuiste",
        "usted": "fue",
        "él": "fue",
        "ella": "fue",
        "nosotros": "fuimos",
        "nosotras": "fuimos",
        "vosotros": "fuisteis",
        "vosotras": "fuisteis",
        "ustedes": "fueron",
        "ellos": "fueron",
        "ellas": "fueron",
    }

def test_indicative_future():
    verb = IrregularToBeExisting()
    assert verb.indicative_future("yo") == "seré"
    assert verb.indicative_future() == {
        "yo": "seré",
        "tú": "serás",
        "vos": "serás",
        "usted": "será",
        "él": "será",
        "ella": "será",
        "nosotros": "seremos",
        "nosotras": "seremos",
        "vosotros": "seréis",
        "vosotras": "seréis",
        "ustedes": "serán",
        "ellos": "serán",
        "ellas": "serán",
    }

def test_indicative_conditional():
    verb = IrregularToBeExisting()
    assert verb.indicative_conditional("yo") == "sería"
    assert verb.indicative_conditional() == {
        "yo": "sería",
        "tú": "serías",
        "vos": "serías",
        "usted": "sería",
        "él": "sería",
        "ella": "sería",
        "nosotros": "seríamos",
        "nosotras": "seríamos",
        "vosotros": "seríais",
        "vosotras": "seríais",
        "ustedes": "serían",
        "ellos": "serían",
        "ellas": "serían",
    }

def test_indicative_present_perfect():
    verb = IrregularToBeExisting()
    assert verb.indicative_present_perfect("yo") == "he sido"
    assert verb.indicative_present_perfect() == {
        "yo": "he sido",
        "tú": "has sido",
        "vos": "has sido",
        "usted": "ha sido",
        "él": "ha sido",
        "ella": "ha sido",
        "nosotros": "hemos sido",
        "nosotras": "hemos sido",
        "vosotros": "habéis sido",
        "vosotras": "habéis sido",
        "ustedes": "han sido",
        "ellos": "han sido",
        "ellas": "han sido",
    }

def test_indicative_past_perfect():
    verb = IrregularToBeExisting()
    assert verb.indicative_past_perfect("yo") == "había sido"
    assert verb.indicative_past_perfect() == {
        "yo": "había sido",
        "tú": "habías sido",
        "vos": "habías sido",
        "usted": "había sido",
        "él": "había sido",
        "ella": "había sido",
        "nosotros": "habíamos sido",
        "nosotras": "habíamos sido",
        "vosotros": "habíais sido",
        "vosotras": "habíais sido",
        "ustedes": "habían sido",
        "ellos": "habían sido",
        "ellas": "habían sido",
    }

def test_indicative_past_anterior():
    verb = IrregularToBeExisting()
    assert verb.indicative_past_anterior("yo") == "hube sido"
    assert verb.indicative_past_anterior() == {
        "yo": "hube sido",
        "tú": "hubiste sido",
        "vos": "hubiste sido",
        "usted": "hubo sido",
        "él": "hubo sido",
        "ella": "hubo sido",
        "nosotros": "hubimos sido",
        "nosotras": "hubimos sido",
        "vosotros": "hubisteis sido",
        "vosotras": "hubisteis sido",
        "ustedes": "hubieron sido",
        "ellos": "hubieron sido",
        "ellas": "hubieron sido",
    }

def test_indicative_future_perfect():
    verb = IrregularToBeExisting()
    assert verb.indicative_future_perfect("yo") == "habré sido"
    assert verb.indicative_future_perfect() == {
        "yo": "habré sido",
        "tú": "habrás sido",
        "vos": "habrás sido",
        "usted": "habrá sido",
        "él": "habrá sido",
        "ella": "habrá sido",
        "nosotros": "habremos sido",
        "nosotras": "habremos sido",
        "vosotros": "habréis sido",
        "vosotras": "habréis sido",
        "ustedes": "habrán sido",
        "ellos": "habrán sido",
        "ellas": "habrán sido",
    }

def test_indicative_conditional_perfect():
    verb = IrregularToBeExisting()
    assert verb.indicative_conditional_perfect("yo") == "habría sido"
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría sido",
        "tú": "habrías sido",
        "vos": "habrías sido",
        "usted": "habría sido",
        "él": "habría sido",
        "ella": "habría sido",
        "nosotros": "habríamos sido",
        "nosotras": "habríamos sido",
        "vosotros": "habríais sido",
        "vosotras": "habríais sido",
        "ustedes": "habrían sido",
        "ellos": "habrían sido",
        "ellas": "habrían sido",
    }

def test_subjunctive_present():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_present("yo") == "sea"
    assert verb.subjunctive_present() == {
        "yo": "sea",
        "tú": "seas",
        "vos": "seas",
        "usted": "sea",
        "él": "sea",
        "ella": "sea",
        "nosotros": "seamos",
        "nosotras": "seamos",
        "vosotros": "seáis",
        "vosotras": "eáis",
        "ustedes": "sean",
        "ellos": "sean",
        "ellas": "sean",
    }

def test_subjunctive_imperfect_preterite():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_imperfect_preterite("yo") == "fuera"
    assert verb.subjunctive_imperfect_preterite() == {
        "yo": "fuera",
        "tú": "fueras",
        "vos": "fueras",
        "usted": "fuera",
        "él": "fuera",
        "ella": "fuera",
        "nosotros": "fuéramos",
        "nosotras": "fuéramos",
        "vosotros": "fuerais",
        "vosotras": "fuerais",
        "ustedes": "fueran",
        "ellos": "fueran",
        "ellas": "fueran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_imperfect_preterite_alternate("yo") == "fuese"
    assert verb.subjunctive_imperfect_preterite_alternate() == {
        "yo": "fuese",
        "tú": "fueses",
        "vos": "fueses",
        "usted": "fuese",
        "él": "fuese",
        "ella": "fuese",
        "nosotros": "fuésemos",
        "nosotras": "fuésemos",
        "vosotros": "fueseis",
        "vosotras": "fueseis",
        "ustedes": "fuesen",
        "ellos": "fuesen",
        "ellas": "fuesen",
    }

def test_subjunctive_future():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_future("yo") == "fuere"
    assert verb.subjunctive_future() == {
        "yo": "fuere",
        "tú": "fueres",
        "vos": "fueres",
        "usted": "fuere",
        "él": "fuere",
        "ella": "fuere",
        "nosotros": "fuéremos",
        "nosotras": "fuéremos",
        "vosotros": "fuereis",
        "vosotras": "fuereis",
        "ustedes": "fueren",
        "ellos": "fueren",
        "ellas": "fueren",
    }

def test_subjunctive_present_perfect():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_present_perfect("yo") == "haya sido"
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya sido",
        "tú": "hayas sido",
        "vos": "hayas sido",
        "usted": "haya sido",
        "él": "haya sido",
        "ella": "haya sido",
        "nosotros": "hayamos sido",
        "nosotras": "hayamos sido",
        "vosotros": "hayáis sido",
        "vosotras": "hayáis sido",
        "ustedes": "hayan sido",
        "ellos": "hayan sido",
        "ellas": "hayan sido",
    }

def test_subjunctive_past_perfect():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_past_perfect("yo") == "hubiera sido"
    assert verb.subjunctive_past_perfect() == {
        "yo": "hubiera sido",
        "tú": "hubieras sido",
        "vos": "hubieras sido",
        "usted": "hubiera sido",
        "él": "hubiera sido",
        "ella": "hubiera sido",
        "nosotros": "hubiéramos sido",
        "nosotras": "hubiéramos sido",
        "vosotros": "hubierais sido",
        "vosotras": "hubierais sido",
        "ustedes": "hubieran sido",
        "ellos": "hubieran sido",
        "ellas": "hubieran sido",
    }

def test_subjunctive_past_perfect_alternate():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_past_perfect_alternate("yo") == "hubiese sido"
    assert verb.subjunctive_past_perfect_alternate() == {
        "yo": "hubiese sido",
        "tú": "hubieses sido",
        "vos": "hubieses sido",
        "usted": "hubiese sido",
        "él": "hubiese sido",
        "ella": "hubiese sido",
        "nosotros": "hubiésemos sido",
        "nosotras": "hubiésemos sido",
        "vosotros": "hubieseis sido",
        "vosotras": "hubieseis sido",
        "ustedes": "hubiesen sido",
        "ellos": "hubiesen sido",
        "ellas": "hubiesen sido",
    }

def test_subjunctive_future_perfect():
    verb = IrregularToBeExisting()
    assert verb.subjunctive_future_perfect("yo") == "hubiere sido"
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere sido",
        "tú": "hubieres sido",
        "vos": "hubieres sido",
        "usted": "hubiere sido",
        "él": "hubiere sido",
        "ella": "hubiere sido",
        "nosotros": "hubiéremos sido",
        "nosotras": "hubiéremos sido",
        "vosotros": "hubiereis sido",
        "vosotras": "hubiereis sido",
        "ustedes": "hubieren sido",
        "ellos": "hubieren sido",
        "ellas": "hubieren sido",
    }

def test_imperative_affirmative():
    verb = IrregularToBeExisting()
    assert verb.imperative_affirmative("tú") == "sé"
    assert verb.imperative_affirmative() == {
        "tú": "sé",
        "vos": "sé",
        "usted": "sea",
        "nosotros": "seamos",
        "nosotras": "seamos",
        "vosotros": "sed",
        "vosotras": "sed",
        "ustedes": "sean",
    }

def test_imperative_negative():
    verb = IrregularToBeExisting()
    assert verb.imperative_negative("tú") == "seas"
    assert verb.imperative_negative() == {
        "tú": "seas",
        "vos": "seás",
        "usted": "sea",
        "nosotros": "seamos",
        "nosotras": "seamos",
        "vosotros": "seáis",
        "vosotras": "seáis",
        "ustedes": "sean",
    }
