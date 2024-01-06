from exprimidora import ModelRequest

def test_participle_and_gerund():
    verb = ModelRequest("conseguir")
    assert verb.gerund() == "consiguiendo"
    assert verb.participle() == "conseguido"

def test_indicative_present():
    verb = ModelRequest("conseguir")
    assert verb.indicative_present("yo") == "consigo"
    assert verb.indicative_present() == {
        "yo": "consigo",
        "tú": "consigues",
        "vos": "conseguís",
        "usted": "consigue",
        "él": "consigue",
        "ella": "consigue",
        "nosotros": "conseguimos",
        "nosotras": "conseguimos",
        "vosotros": "conseguís",
        "vosotras": "conseguís",
        "ustedes": "consiguen",
        "ellos": "consiguen",
        "ellas": "consiguen",
    }

def test_indicative_imperfect():
    verb = ModelRequest("conseguir")
    assert verb.indicative_imperfect("yo") == "conseguía"
    assert verb.indicative_imperfect() == {
        "yo": "conseguía",
        "tú": "conseguías",
        "vos": "conseguías",
        "usted": "conseguía",
        "él": "conseguía",
        "ella": "conseguía",
        "nosotros": "conseguíamos",
        "nosotras": "conseguíamos",
        "vosotros": "conseguíais",
        "vosotras": "conseguíais",
        "ustedes": "conseguían",
        "ellos": "conseguían",
        "ellas": "conseguían",
    }

def test_indicative_preterite():
    verb = ModelRequest("conseguir")
    assert verb.indicative_preterite("yo") == "conseguí"
    assert verb.indicative_preterite() == {
        "yo": "conseguí",
        "tú": "conseguiste",
        "vos": "conseguiste",
        "usted": "consiguió",
        "él": "consiguió",
        "ella": "consiguió",
        "nosotros": "conseguimos",
        "nosotras": "conseguimos",
        "vosotros": "conseguisteis",
        "vosotras": "conseguisteis",
        "ustedes": "consiguieron",
        "ellos": "consiguieron",
        "ellas": "consiguieron",
    }

def test_indicative_future():
    verb = ModelRequest("conseguir")
    assert verb.indicative_future("yo") == "conseguiré"
    assert verb.indicative_future() == {
        "yo": "conseguiré",
        "tú": "conseguirás",
        "vos": "conseguirás",
        "usted": "conseguirá",
        "él": "conseguirá",
        "ella": "conseguirá",
        "nosotros": "conseguiremos",
        "nosotras": "conseguiremos",
        "vosotros": "conseguiréis",
        "vosotras": "conseguiréis",
        "ustedes": "conseguirán",
        "ellos": "conseguirán",
        "ellas": "conseguirán",
    }

def test_indicative_conditional():
    verb = ModelRequest("conseguir")
    assert verb.indicative_conditional("yo") == "conseguiría"
    assert verb.indicative_conditional() == {
        "yo": "conseguiría",
        "tú": "conseguirías",
        "vos": "conseguirías",
        "usted": "conseguiría",
        "él": "conseguiría",
        "ella": "conseguiría",
        "nosotros": "conseguiríamos",
        "nosotras": "conseguiríamos",
        "vosotros": "conseguiríais",
        "vosotras": "conseguiríais",
        "ustedes": "conseguirían",
        "ellos": "conseguirían",
        "ellas": "conseguirían",
    }

def test_indicative_present_perfect():
    verb = ModelRequest("conseguir")
    assert verb.indicative_present_perfect("yo") == "he conseguido"
    assert verb.indicative_present_perfect() == {
        "yo": "he conseguido",
        "tú": "has conseguido",
        "vos": "has conseguido",
        "usted": "ha conseguido",
        "él": "ha conseguido",
        "ella": "ha conseguido",
        "nosotros": "hemos conseguido",
        "nosotras": "hemos conseguido",
        "vosotros": "habéis conseguido",
        "vosotras": "habéis conseguido",
        "ustedes": "han conseguido",
        "ellos": "han conseguido",
        "ellas": "han conseguido",
    }

def test_indicative_past_perfect():
    verb = ModelRequest("conseguir")
    assert verb.indicative_past_perfect("yo") == "había conseguido"
    assert verb.indicative_past_perfect() == {
        "yo": "había conseguido",
        "tú": "habías conseguido",
        "vos": "habías conseguido",
        "usted": "había conseguido",
        "él": "había conseguido",
        "ella": "había conseguido",
        "nosotros": "habíamos conseguido",
        "nosotras": "habíamos conseguido",
        "vosotros": "habíais conseguido",
        "vosotras": "habíais conseguido",
        "ustedes": "habían conseguido",
        "ellos": "habían conseguido",
        "ellas": "habían conseguido",
    }

def test_indicative_past_anterior():
    verb = ModelRequest("conseguir")
    assert verb.indicative_past_anterior("yo") == "hube conseguido"
    assert verb.indicative_past_anterior() == {
        "yo": "hube conseguido",
        "tú": "hubiste conseguido",
        "vos": "hubiste conseguido",
        "usted": "hubo conseguido",
        "él": "hubo conseguido",
        "ella": "hubo conseguido",
        "nosotros": "hubimos conseguido",
        "nosotras": "hubimos conseguido",
        "vosotros": "hubisteis conseguido",
        "vosotras": "hubisteis conseguido",
        "ustedes": "hubieron conseguido",
        "ellos": "hubieron conseguido",
        "ellas": "hubieron conseguido",
    }

def test_indicative_future_perfect():
    verb = ModelRequest("conseguir")
    assert verb.indicative_future_perfect("yo") == "habré conseguido"
    assert verb.indicative_future_perfect() == {
        "yo": "habré conseguido",
        "tú": "habrás conseguido",
        "vos": "habrás conseguido",
        "usted": "habrá conseguido",
        "él": "habrá conseguido",
        "ella": "habrá conseguido",
        "nosotros": "habremos conseguido",
        "nosotras": "habremos conseguido",
        "vosotros": "habréis conseguido",
        "vosotras": "habréis conseguido",
        "ustedes": "habrán conseguido",
        "ellos": "habrán conseguido",
        "ellas": "habrán conseguido",
    }

def test_indicative_conditional_perfect():
    verb = ModelRequest("conseguir")
    assert verb.indicative_conditional_perfect("yo") == "habría conseguido"
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría conseguido",
        "tú": "habrías conseguido",
        "vos": "habrías conseguido",
        "usted": "habría conseguido",
        "él": "habría conseguido",
        "ella": "habría conseguido",
        "nosotros": "habríamos conseguido",
        "nosotras": "habríamos conseguido",
        "vosotros": "habríais conseguido",
        "vosotras": "habríais conseguido",
        "ustedes": "habrían conseguido",
        "ellos": "habrían conseguido",
        "ellas": "habrían conseguido",
    }

def test_subjunctive_present():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_present("yo") == "consiga"
    assert verb.subjunctive_present() == {
        "yo": "consiga",
        "tú": "consigas",
        "vos": "consigás",
        "usted": "consiga",
        "él": "consiga",
        "ella": "consiga",
        "nosotros": "consigamos",
        "nosotras": "consigamos",
        "vosotros": "consigáis",
        "vosotras": "consigáis",
        "ustedes": "consigan",
        "ellos": "consigan",
        "ellas": "consigan",
    }

def test_subjunctive_imperfect_preterite():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_imperfect_preterite("yo") == "consiguiera"
    assert verb.subjunctive_imperfect_preterite() == {
        "yo": "consiguiera",
        "tú": "consiguieras",
        "vos": "consiguieras",
        "usted": "consiguiera",
        "él": "consiguiera",
        "ella": "consiguiera",
        "nosotros": "consiguiéramos",
        "nosotras": "consiguiéramos",
        "vosotros": "consiguierais",
        "vosotras": "consiguierais",
        "ustedes": "consiguieran",
        "ellos": "consiguieran",
        "ellas": "consiguieran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_imperfect_preterite_alternate("yo") == "consiguiese"
    assert verb.subjunctive_imperfect_preterite_alternate() == {
        "yo": "consiguiese",
        "tú": "consiguieses",
        "vos": "consiguieses",
        "usted": "consiguiese",
        "él": "consiguiese",
        "ella": "consiguiese",
        "nosotros": "consiguiésemos",
        "nosotras": "consiguiésemos",
        "vosotros": "consiguieseis",
        "vosotras": "consiguieseis",
        "ustedes": "consiguiesen",
        "ellos": "consiguiesen",
        "ellas": "consiguiesen",
    }

def test_subjunctive_future():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_future("yo") == "consiguiere"
    assert verb.subjunctive_future() == {
        "yo": "consiguiere",
        "tú": "consiguieres",
        "vos": "consiguieres",
        "usted": "consiguiere",
        "él": "consiguiere",
        "ella": "consiguiere",
        "nosotros": "consiguiéremos",
        "nosotras": "consiguiéremos",
        "vosotros": "consiguiereis",
        "vosotras": "consiguiereis",
        "ustedes": "consiguieren",
        "ellos": "consiguieren",
        "ellas": "consiguieren",
    }

def test_subjunctive_present_perfect():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_present_perfect("yo") == "haya conseguido"
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya conseguido",
        "tú": "hayas conseguido",
        "vos": "hayas conseguido",
        "usted": "haya conseguido",
        "él": "haya conseguido",
        "ella": "haya conseguido",
        "nosotros": "hayamos conseguido",
        "nosotras": "hayamos conseguido",
        "vosotros": "hayáis conseguido",
        "vosotras": "hayáis conseguido",
        "ustedes": "hayan conseguido",
        "ellos": "hayan conseguido",
        "ellas": "hayan conseguido",
    }

def test_subjunctive_past_perfect():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_past_perfect("yo") == "hubiera conseguido"
    assert verb.subjunctive_past_perfect() == {
        "yo": "hubiera conseguido",
        "tú": "hubieras conseguido",
        "vos": "hubieras conseguido",
        "usted": "hubiera conseguido",
        "él": "hubiera conseguido",
        "ella": "hubiera conseguido",
        "nosotros": "hubiéramos conseguido",
        "nosotras": "hubiéramos conseguido",
        "vosotros": "hubierais conseguido",
        "vosotras": "hubierais conseguido",
        "ustedes": "hubieran conseguido",
        "ellos": "hubieran conseguido",
        "ellas": "hubieran conseguido",
    }

def test_subjunctive_past_perfect_alternate():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_past_perfect_alternate("yo") == "hubiese conseguido"
    assert verb.subjunctive_past_perfect_alternate() == {
        "yo": "hubiese conseguido",
        "tú": "hubieses conseguido",
        "vos": "hubieses conseguido",
        "usted": "hubiese conseguido",
        "él": "hubiese conseguido",
        "ella": "hubiese conseguido",
        "nosotros": "hubiésemos conseguido",
        "nosotras": "hubiésemos conseguido",
        "vosotros": "hubieseis conseguido",
        "vosotras": "hubieseis conseguido",
        "ustedes": "hubiesen conseguido",
        "ellos": "hubiesen conseguido",
        "ellas": "hubiesen conseguido",
    }

def test_subjunctive_future_perfect():
    verb = ModelRequest("conseguir")
    assert verb.subjunctive_future_perfect("yo") == "hubiere conseguido"
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere conseguido",
        "tú": "hubieres conseguido",
        "vos": "hubieres conseguido",
        "usted": "hubiere conseguido",
        "él": "hubiere conseguido",
        "ella": "hubiere conseguido",
        "nosotros": "hubiéremos conseguido",
        "nosotras": "hubiéremos conseguido",
        "vosotros": "hubiereis conseguido",
        "vosotras": "hubiereis conseguido",
        "ustedes": "hubieren conseguido",
        "ellos": "hubieren conseguido",
        "ellas": "hubieren conseguido",
    }

def test_imperative_affirmative():
    verb = ModelRequest("conseguir")
    assert verb.imperative_affirmative("tú") == "consigue"
    assert verb.imperative_affirmative() == {
        "tú": "consigue",
        "vos": "conseguí",
        "usted": "consiga",
        "nosotros": "consigamos",
        "nosotras": "consigamos",
        "vosotros": "conseguid",
        "vosotras": "conseguid",
        "ustedes": "consigan",
    }

def test_imperative_negative():
    verb = ModelRequest("conseguir")
    assert verb.imperative_negative("tú") == "consigas"
    assert verb.imperative_negative() == {
        "tú": "consigas",
        "vos": "consigás",
        "usted": "consiga",
        "nosotros": "consigamos",
        "nosotras": "consigamos",
        "vosotros": "consigáis",
        "vosotras": "consigáis",
        "ustedes": "consigan",
    }
