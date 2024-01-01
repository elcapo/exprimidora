from exprimidora import RegularSecondGroup

def test_root_participle_and_gerund():
    verb = RegularSecondGroup("aprender")
    assert verb.root() == "aprend"
    assert verb.gerund() == "aprendiendo"
    assert verb.participle() == "aprendido"

def test_indicative_present():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_present("yo") == "aprendo"
    assert verb.indicative_present() == {
        "yo": "aprendo",
        "tú": "aprendes",
        "vos": "aprendés",
        "usted": "aprende",
        "él": "aprende",
        "ella": "aprende",
        "nosotros": "aprendemos",
        "nosotras": "aprendemos",
        "vosotros": "aprendéis",
        "vosotras": "aprendéis",
        "ustedes": "aprenden",
        "ellos": "aprenden",
        "ellas": "aprenden",
    }

def test_indicative_imperfect():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_imperfect("yo") == "aprendía"
    assert verb.indicative_imperfect() == {
        "yo": "aprendía",
        "tú": "aprendías",
        "vos": "aprendías",
        "usted": "aprendía",
        "él": "aprendía",
        "ella": "aprendía",
        "nosotros": "aprendíamos",
        "nosotras": "aprendíamos",
        "vosotros": "aprendíais",
        "vosotras": "aprendíais",
        "ustedes": "aprendían",
        "ellos": "aprendían",
        "ellas": "aprendían",
    }

def test_indicative_preterite():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_preterite("yo") == "aprendí"
    assert verb.indicative_preterite() == {
        "yo": "aprendí",
        "tú": "aprendiste",
        "vos": "aprendiste",
        "usted": "aprendió",
        "él": "aprendió",
        "ella": "aprendió",
        "nosotros": "aprendimos",
        "nosotras": "aprendimos",
        "vosotros": "aprendisteis",
        "vosotras": "aprendisteis",
        "ustedes": "aprendieron",
        "ellos": "aprendieron",
        "ellas": "aprendieron",
    }

def test_indicative_future():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_future("yo") == "aprenderé"
    assert verb.indicative_future() == {
        "yo": "aprenderé",
        "tú": "aprenderás",
        "vos": "aprenderás",
        "usted": "aprenderá",
        "él": "aprenderá",
        "ella": "aprenderá",
        "nosotros": "aprenderemos",
        "nosotras": "aprenderemos",
        "vosotros": "aprenderéis",
        "vosotras": "aprenderéis",
        "ustedes": "aprenderán",
        "ellos": "aprenderán",
        "ellas": "aprenderán",
    }

def test_indicative_conditional():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_conditional("yo") == "aprendería"
    assert verb.indicative_conditional() == {
        "yo": "aprendería",
        "tú": "aprenderías",
        "vos": "aprenderías",
        "usted": "aprendería",
        "él": "aprendería",
        "ella": "aprendería",
        "nosotros": "aprenderíamos",
        "nosotras": "aprenderíamos",
        "vosotros": "aprenderíais",
        "vosotras": "aprenderíais",
        "ustedes": "aprenderían",
        "ellos": "aprenderían",
        "ellas": "aprenderían",
    }

def test_indicative_present_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_present_perfect("yo") == "he aprendido"
    assert verb.indicative_present_perfect() == {
        "yo": "he aprendido",
        "tú": "has aprendido",
        "vos": "has aprendido",
        "usted": "ha aprendido",
        "él": "ha aprendido",
        "ella": "ha aprendido",
        "nosotros": "hemos aprendido",
        "nosotras": "hemos aprendido",
        "vosotros": "habéis aprendido",
        "vosotras": "habéis aprendido",
        "ustedes": "han aprendido",
        "ellos": "han aprendido",
        "ellas": "han aprendido",
    }

def test_indicative_past_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_past_perfect("yo") == "había aprendido"
    assert verb.indicative_past_perfect() == {
        "yo": "había aprendido",
        "tú": "habías aprendido",
        "vos": "habías aprendido",
        "usted": "había aprendido",
        "él": "había aprendido",
        "ella": "había aprendido",
        "nosotros": "habíamos aprendido",
        "nosotras": "habíamos aprendido",
        "vosotros": "habíais aprendido",
        "vosotras": "habíais aprendido",
        "ustedes": "habían aprendido",
        "ellos": "habían aprendido",
        "ellas": "habían aprendido",
    }

def test_indicative_past_anterior():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_past_anterior("yo") == "hube aprendido"
    assert verb.indicative_past_anterior() == {
        "yo": "hube aprendido",
        "tú": "hubiste aprendido",
        "vos": "hubiste aprendido",
        "usted": "hubo aprendido",
        "él": "hubo aprendido",
        "ella": "hubo aprendido",
        "nosotros": "hubimos aprendido",
        "nosotras": "hubimos aprendido",
        "vosotros": "hubisteis aprendido",
        "vosotras": "hubisteis aprendido",
        "ustedes": "hubieron aprendido",
        "ellos": "hubieron aprendido",
        "ellas": "hubieron aprendido",
    }

def test_indicative_future_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_future_perfect("yo") == "habré aprendido"
    assert verb.indicative_future_perfect() == {
        "yo": "habré aprendido",
        "tú": "habrás aprendido",
        "vos": "habrás aprendido",
        "usted": "habrá aprendido",
        "él": "habrá aprendido",
        "ella": "habrá aprendido",
        "nosotros": "habremos aprendido",
        "nosotras": "habremos aprendido",
        "vosotros": "habréis aprendido",
        "vosotras": "habréis aprendido",
        "ustedes": "habrán aprendido",
        "ellos": "habrán aprendido",
        "ellas": "habrán aprendido",
    }

def test_indicative_conditional_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.indicative_conditional_perfect("yo") == "habría aprendido"
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría aprendido",
        "tú": "habrías aprendido",
        "vos": "habrías aprendido",
        "usted": "habría aprendido",
        "él": "habría aprendido",
        "ella": "habría aprendido",
        "nosotros": "habríamos aprendido",
        "nosotras": "habríamos aprendido",
        "vosotros": "habríais aprendido",
        "vosotras": "habríais aprendido",
        "ustedes": "habrían aprendido",
        "ellos": "habrían aprendido",
        "ellas": "habrían aprendido",
    }

def test_subjunctive_present():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_present("yo") == "aprenda"
    assert verb.subjunctive_present() == {
        "yo": "aprenda",
        "tú": "aprendas",
        "vos": "aprendás",
        "usted": "aprenda",
        "él": "aprenda",
        "ella": "aprenda",
        "nosotros": "aprendamos",
        "nosotras": "aprendamos",
        "vosotros": "aprendáis",
        "vosotras": "aprendáis",
        "ustedes": "aprendan",
        "ellos": "aprendan",
        "ellas": "aprendan",
    }

def test_subjunctive_imperfect_preterite():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_imperfect_preterite("yo") == "aprendiera"
    assert verb.subjunctive_imperfect_preterite() == {
        "yo": "aprendiera",
        "tú": "aprendieras",
        "vos": "aprendieras",
        "usted": "aprendiera",
        "él": "aprendiera",
        "ella": "aprendiera",
        "nosotros": "aprendiéramos",
        "nosotras": "aprendiéramos",
        "vosotros": "aprendierais",
        "vosotras": "aprendierais",
        "ustedes": "aprendieran",
        "ellos": "aprendieran",
        "ellas": "aprendieran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_imperfect_preterite_alternate("yo") == "aprendiese"
    assert verb.subjunctive_imperfect_preterite_alternate() == {
        "yo": "aprendiese",
        "tú": "aprendieses",
        "vos": "aprendieses",
        "usted": "aprendiese",
        "él": "aprendiese",
        "ella": "aprendiese",
        "nosotros": "aprendiésemos",
        "nosotras": "aprendiésemos",
        "vosotros": "aprendieseis",
        "vosotras": "aprendieseis",
        "ustedes": "aprendiesen",
        "ellos": "aprendiesen",
        "ellas": "aprendiesen",
    }

def test_subjunctive_future():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_future("yo") == "aprendiere"
    assert verb.subjunctive_future() == {
        "yo": "aprendiere",
        "tú": "aprendieres",
        "vos": "aprendieres",
        "usted": "aprendiere",
        "él": "aprendiere",
        "ella": "aprendiere",
        "nosotros": "aprendiéremos",
        "nosotras": "aprendiéremos",
        "vosotros": "aprendiereis",
        "vosotras": "aprendiereis",
        "ustedes": "aprendieren",
        "ellos": "aprendieren",
        "ellas": "aprendieren",
    }

def test_subjunctive_present_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_present_perfect("yo") == "haya aprendido"
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya aprendido",
        "tú": "hayas aprendido",
        "vos": "hayas aprendido",
        "usted": "haya aprendido",
        "él": "haya aprendido",
        "ella": "haya aprendido",
        "nosotros": "hayamos aprendido",
        "nosotras": "hayamos aprendido",
        "vosotros": "hayáis aprendido",
        "vosotras": "hayáis aprendido",
        "ustedes": "hayan aprendido",
        "ellos": "hayan aprendido",
        "ellas": "hayan aprendido",
    }

def test_subjunctive_past_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_past_perfect("yo") == "hubiera aprendido"
    assert verb.subjunctive_past_perfect() == {
        "yo": "hubiera aprendido",
        "tú": "hubieras aprendido",
        "vos": "hubieras aprendido",
        "usted": "hubiera aprendido",
        "él": "hubiera aprendido",
        "ella": "hubiera aprendido",
        "nosotros": "hubiéramos aprendido",
        "nosotras": "hubiéramos aprendido",
        "vosotros": "hubierais aprendido",
        "vosotras": "hubierais aprendido",
        "ustedes": "hubieran aprendido",
        "ellos": "hubieran aprendido",
        "ellas": "hubieran aprendido",
    }

def test_subjunctive_past_perfect_alternate():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_past_perfect_alternate("yo") == "hubiese aprendido"
    assert verb.subjunctive_past_perfect_alternate() == {
        "yo": "hubiese aprendido",
        "tú": "hubieses aprendido",
        "vos": "hubieses aprendido",
        "usted": "hubiese aprendido",
        "él": "hubiese aprendido",
        "ella": "hubiese aprendido",
        "nosotros": "hubiésemos aprendido",
        "nosotras": "hubiésemos aprendido",
        "vosotros": "hubieseis aprendido",
        "vosotras": "hubieseis aprendido",
        "ustedes": "hubiesen aprendido",
        "ellos": "hubiesen aprendido",
        "ellas": "hubiesen aprendido",
    }

def test_subjunctive_future_perfect():
    verb = RegularSecondGroup("aprender")
    assert verb.subjunctive_future_perfect("yo") == "hubiere aprendido"
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere aprendido",
        "tú": "hubieres aprendido",
        "vos": "hubieres aprendido",
        "usted": "hubiere aprendido",
        "él": "hubiere aprendido",
        "ella": "hubiere aprendido",
        "nosotros": "hubiéremos aprendido",
        "nosotras": "hubiéremos aprendido",
        "vosotros": "hubiereis aprendido",
        "vosotras": "hubiereis aprendido",
        "ustedes": "hubieren aprendido",
        "ellos": "hubieren aprendido",
        "ellas": "hubieren aprendido",
    }

def test_imperative_affirmative():
    verb = RegularSecondGroup("aprender")
    assert verb.imperative_affirmative("tú") == "aprende"
    assert verb.imperative_affirmative() == {
        "tú": "aprende",
        "vos": "aprendé",
        "usted": "aprenda",
        "nosotros": "aprendamos",
        "nosotras": "aprendamos",
        "vosotros": "aprended",
        "vosotras": "aprended",
        "ustedes": "aprendan",
    }

def test_imperative_negative():
    verb = RegularSecondGroup("aprender")
    assert verb.imperative_negative("tú") == "aprendas"
    assert verb.imperative_negative() == {
        "tú": "aprendas",
        "vos": "aprendás",
        "usted": "aprenda",
        "nosotros": "aprendamos",
        "nosotras": "aprendamos",
        "vosotros": "aprendáis",
        "vosotras": "aprendáis",
        "ustedes": "aprendan",
    }
