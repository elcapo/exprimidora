from exprimidora import IrregularToHave

def test_participle_and_gerund():
    verb = IrregularToHave()
    assert verb.gerund() == "habiendo"
    assert verb.participle() == "habido"

def test_indicative_present():
    verb = IrregularToHave()
    assert verb.indicative_present() == {
        "yo": "he",
        "tú": "has",
        "vos": "has",
        "usted": "ha",
        "él": "ha",
        "ella": "ha",
        "nosotros": "hemos",
        "nosotras": "hemos",
        "vosotros": "habéis",
        "vosotras": "habéis",
        "ustedes": "han",
        "ellos": "han",
        "ellas": "han",
    }

def test_indicative_imperfect():
    verb = IrregularToHave()
    assert verb.indicative_imperfect() == {
        "yo": "había",
        "tú": "habías",
        "vos": "habías",
        "usted": "había",
        "él": "había",
        "ella": "había",
        "nosotros": "habíamos",
        "nosotras": "habíamos",
        "vosotros": "habíais",
        "vosotras": "habíais",
        "ustedes": "habían",
        "ellos": "habían",
        "ellas": "habían",
    }

def test_indicative_preterite():
    verb = IrregularToHave()
    assert verb.indicative_preterite() == {
        "yo": "hube",
        "tú": "hubiste",
        "vos": "hubiste",
        "usted": "hubo",
        "él": "hubo",
        "ella": "hubo",
        "nosotros": "hubimos",
        "nosotras": "hubimos",
        "vosotros": "hubisteis",
        "vosotras": "hubisteis",
        "ustedes": "hubieron",
        "ellos": "hubieron",
        "ellas": "hubieron",
    }

def test_indicative_future():
    verb = IrregularToHave()
    assert verb.indicative_future() == {
        "yo": "habré",
        "tú": "habrás",
        "vos": "habrás",
        "usted": "habrá",
        "él": "habrá",
        "ella": "habrá",
        "nosotros": "habremos",
        "nosotras": "habremos",
        "vosotros": "habréis",
        "vosotras": "habréis",
        "ustedes": "habrán",
        "ellos": "habrán",
        "ellas": "habrán",
    }

def test_indicative_conditional():
    verb = IrregularToHave()
    assert verb.indicative_conditional() == {
        "yo": "habría",
        "tú": "habrías",
        "vos": "habrías",
        "usted": "habría",
        "él": "habría",
        "ella": "habría",
        "nosotros": "habríamos",
        "nosotras": "habríamos",
        "vosotros": "habríais",
        "vosotras": "habríais",
        "ustedes": "habrían",
        "ellos": "habrían",
        "ellas": "habrían",
    }

def test_indicative_present_perfect():
    verb = IrregularToHave()
    assert verb.indicative_present_perfect() == {
        "yo": "he habido",
        "tú": "has habido",
        "vos": "has habido",
        "usted": "ha habido",
        "él": "ha habido",
        "ella": "ha habido",
        "nosotros": "hemos habido",
        "nosotras": "hemos habido",
        "vosotros": "habéis habido",
        "vosotras": "habéis habido",
        "ustedes": "han habido",
        "ellos": "han habido",
        "ellas": "han habido",
    }

def test_indicative_past_perfect():
    verb = IrregularToHave()
    assert verb.indicative_past_perfect() == {
        "yo": "había habido",
        "tú": "habías habido",
        "vos": "habías habido",
        "usted": "había habido",
        "él": "había habido",
        "ella": "había habido",
        "nosotros": "habíamos habido",
        "nosotras": "habíamos habido",
        "vosotros": "habíais habido",
        "vosotras": "habíais habido",
        "ustedes": "habían habido",
        "ellos": "habían habido",
        "ellas": "habían habido",
    }

def test_indicative_past_anterior():
    verb = IrregularToHave()
    assert verb.indicative_past_anterior() == {
        "yo": "hube habido",
        "tú": "hubiste habido",
        "vos": "hubiste habido",
        "usted": "hubo habido",
        "él": "hubo habido",
        "ella": "hubo habido",
        "nosotros": "hubimos habido",
        "nosotras": "hubimos habido",
        "vosotros": "hubisteis habido",
        "vosotras": "hubisteis habido",
        "ustedes": "hubieron habido",
        "ellos": "hubieron habido",
        "ellas": "hubieron habido",
    }

def test_indicative_future_perfect():
    verb = IrregularToHave()
    assert verb.indicative_future_perfect() == {
        "yo": "habré habido",
        "tú": "habrás habido",
        "vos": "habrás habido",
        "usted": "habrá habido",
        "él": "habrá habido",
        "ella": "habrá habido",
        "nosotros": "habremos habido",
        "nosotras": "habremos habido",
        "vosotros": "habréis habido",
        "vosotras": "habréis habido",
        "ustedes": "habrán habido",
        "ellos": "habrán habido",
        "ellas": "habrán habido",
    }

def test_indicative_conditional_perfect():
    verb = IrregularToHave()
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría habido",
        "tú": "habrías habido",
        "vos": "habrías habido",
        "usted": "habría habido",
        "él": "habría habido",
        "ella": "habría habido",
        "nosotros": "habríamos habido",
        "nosotras": "habríamos habido",
        "vosotros": "habríais habido",
        "vosotras": "habríais habido",
        "ustedes": "habrían habido",
        "ellos": "habrían habido",
        "ellas": "habrían habido",
    }

def test_subjunctive_present():
    verb = IrregularToHave()
    assert verb.subjunctive_present() == {
        "yo": "haya",
        "tú": "hayas",
        "vos": "hayas",
        "usted": "haya",
        "él": "haya",
        "ella": "haya",
        "nosotros": "hayamos",
        "nosotras": "hayamos",
        "vosotros": "hayáis",
        "vosotras": "hayáis",
        "ustedes": "hayan",
        "ellos": "hayan",
        "ellas": "hayan",
    }

def test_subjunctive_imperfect_preterite():
    verb = IrregularToHave()
    assert verb.subjunctive_imperfect_preterite(alternate_form = False) == {
        "yo": "hubiera",
        "tú": "hubieras",
        "vos": "hubieras",
        "usted": "hubiera",
        "él": "hubiera",
        "ella": "hubiera",
        "nosotros": "hubiéramos",
        "nosotras": "hubiéramos",
        "vosotros": "hubierais",
        "vosotras": "hubierais",
        "ustedes": "hubieran",
        "ellos": "hubieran",
        "ellas": "hubieran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = IrregularToHave()
    assert verb.subjunctive_imperfect_preterite(alternate_form = True) == {
        "yo": "hubiese",
        "tú": "hubieses",
        "vos": "hubieses",
        "usted": "hubiese",
        "él": "hubiese",
        "ella": "hubiese",
        "nosotros": "hubiésemos",
        "nosotras": "hubiésemos",
        "vosotros": "hubieseis",
        "vosotras": "hubieseis",
        "ustedes": "hubiesen",
        "ellos": "hubiesen",
        "ellas": "hubiesen",
    }

def test_subjunctive_future():
    verb = IrregularToHave()
    assert verb.subjunctive_future() == {
        "yo": "hubiere",
        "tú": "hubieres",
        "vos": "hubieres",
        "usted": "hubiere",
        "él": "hubiere",
        "ella": "hubiere",
        "nosotros": "hubiéremos",
        "nosotras": "hubiéremos",
        "vosotros": "hubiereis",
        "vosotras": "hubiereis",
        "ustedes": "hubieren",
        "ellos": "hubieren",
        "ellas": "hubieren",
    }

def test_subjunctive_present_perfect():
    verb = IrregularToHave()
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya habido",
        "tú": "hayas habido",
        "vos": "hayas habido",
        "usted": "haya habido",
        "él": "haya habido",
        "ella": "haya habido",
        "nosotros": "hayamos habido",
        "nosotras": "hayamos habido",
        "vosotros": "hayáis habido",
        "vosotras": "hayáis habido",
        "ustedes": "hayan habido",
        "ellos": "hayan habido",
        "ellas": "hayan habido",
    }

def test_subjunctive_past_perfect():
    verb = IrregularToHave()
    assert verb.subjunctive_past_perfect(alternate_form = False) == {
        "yo": "hubiera habido",
        "tú": "hubieras habido",
        "vos": "hubieras habido",
        "usted": "hubiera habido",
        "él": "hubiera habido",
        "ella": "hubiera habido",
        "nosotros": "hubiéramos habido",
        "nosotras": "hubiéramos habido",
        "vosotros": "hubierais habido",
        "vosotras": "hubierais habido",
        "ustedes": "hubieran habido",
        "ellos": "hubieran habido",
        "ellas": "hubieran habido",
    }

def test_subjunctive_past_perfect_alternate():
    verb = IrregularToHave()
    assert verb.subjunctive_past_perfect(alternate_form = True) == {
        "yo": "hubiese habido",
        "tú": "hubieses habido",
        "vos": "hubieses habido",
        "usted": "hubiese habido",
        "él": "hubiese habido",
        "ella": "hubiese habido",
        "nosotros": "hubiésemos habido",
        "nosotras": "hubiésemos habido",
        "vosotros": "hubieseis habido",
        "vosotras": "hubieseis habido",
        "ustedes": "hubiesen habido",
        "ellos": "hubiesen habido",
        "ellas": "hubiesen habido",
    }

def test_subjunctive_future_perfect():
    verb = IrregularToHave()
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere habido",
        "tú": "hubieres habido",
        "vos": "hubieres habido",
        "usted": "hubiere habido",
        "él": "hubiere habido",
        "ella": "hubiere habido",
        "nosotros": "hubiéremos habido",
        "nosotras": "hubiéremos habido",
        "vosotros": "hubiereis habido",
        "vosotras": "hubiereis habido",
        "ustedes": "hubieren habido",
        "ellos": "hubieren habido",
        "ellas": "hubieren habido",
    }

def test_imperative_affirmative():
    verb = IrregularToHave()
    assert verb.imperative_affirmative() == {
        "tú": "he",
        "vos": "he",
        "usted": "haya",
        "nosotros": "hayamos",
        "nosotras": "hayamos",
        "vosotros": "habed",
        "vosotras": "habed",
        "ustedes": "hayan",
    }

def test_imperative_negative():
    verb = IrregularToHave()
    assert verb.imperative_negative() == {
        "tú": "hayas",
        "vos": "hayás",
        "usted": "haya",
        "nosotros": "hayamos",
        "nosotras": "hayamos",
        "vosotros": "hayáis",
        "vosotras": "hayáis",
        "ustedes": "hayan",
    }
