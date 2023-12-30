from exprimidora import RegularFirstGroup

def test_root_participle_and_gerund():
    verb = RegularFirstGroup("amar")
    assert verb.root() == "am"
    assert verb.gerund() == "amando"
    assert verb.participle() == "amado"

def test_indicative_present():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_present() == {
        "yo": "amo",
        "tú": "amas",
        "vos": "amás",
        "usted": "ama",
        "él": "ama",
        "ella": "ama",
        "nosotros": "amamos",
        "nosotras": "amamos",
        "vosotros": "amáis",
        "vosotras": "amáis",
        "ustedes": "aman",
        "ellos": "aman",
        "ellas": "aman"
    }

def test_indicative_imperfect():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_imperfect() == {
        "yo": "amaba",
        "tú": "amabas",
        "vos": "amabas",
        "usted": "amaba",
        "él": "amaba",
        "ella": "amaba",
        "nosotros": "amábamos",
        "nosotras": "amábamos",
        "vosotros": "amabais",
        "vosotras": "amabais",
        "ustedes": "amaban",
        "ellos": "amaban",
        "ellas": "amaban"
    }

def test_indicative_preterite():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_preterite() == {
        "yo": "amé",
        "tú": "amaste",
        "vos": "amaste",
        "usted": "amó",
        "él": "amó",
        "ella": "amó",
        "nosotros": "amamos",
        "nosotras": "amamos",
        "vosotros": "amasteis",
        "vosotras": "amasteis",
        "ustedes": "amaron",
        "ellos": "amaron",
        "ellas": "amaron",
    }

def test_indicative_future():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_future() == {
        "yo": "amaré",
        "tú": "amarás",
        "vos": "amarás",
        "usted": "amará",
        "él": "amará",
        "ella": "amará",
        "nosotros": "amaremos",
        "nosotras": "amaremos",
        "vosotros": "amaréis",
        "vosotras": "amaréis",
        "ustedes": "amarán",
        "ellos": "amarán",
        "ellas": "amarán",
    }

def test_indicative_conditional():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_conditional() == {
        "yo": "amaría",
        "tú": "amarías",
        "vos": "amarías",
        "usted": "amaría",
        "él": "amaría",
        "ella": "amaría",
        "nosotros": "amaríamos",
        "nosotras": "amaríamos",
        "vosotros": "amaríais",
        "vosotras": "amaríais",
        "ustedes": "amarían",
        "ellos": "amarían",
        "ellas": "amarían",
    }

def test_indicative_present_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_present_perfect() == {
        "yo": "he amado",
        "tú": "has amado",
        "vos": "has amado",
        "usted": "ha amado",
        "él": "ha amado",
        "ella": "ha amado",
        "nosotros": "hemos amado",
        "nosotras": "hemos amado",
        "vosotros": "habéis amado",
        "vosotras": "habéis amado",
        "ustedes": "han amado",
        "ellos": "han amado",
        "ellas": "han amado",
    }

def test_indicative_past_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_past_perfect() == {
        "yo": "había amado",
        "tú": "habías amado",
        "vos": "habías amado",
        "usted": "había amado",
        "él": "había amado",
        "ella": "había amado",
        "nosotros": "habíamos amado",
        "nosotras": "habíamos amado",
        "vosotros": "habíais amado",
        "vosotras": "habíais amado",
        "ustedes": "habían amado",
        "ellos": "habían amado",
        "ellas": "habían amado",
    }

def test_indicative_past_anterior():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_past_anterior() == {
        "yo": "hube amado",
        "tú": "hubiste amado",
        "vos": "hubiste amado",
        "usted": "hubo amado",
        "él": "hubo amado",
        "ella": "hubo amado",
        "nosotros": "hubimos amado",
        "nosotras": "hubimos amado",
        "vosotros": "hubisteis amado",
        "vosotras": "hubisteis amado",
        "ustedes": "hubieron amado",
        "ellos": "hubieron amado",
        "ellas": "hubieron amado",
    }

def test_indicative_future_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_future_perfect() == {
        "yo": "habré amado",
        "tú": "habrás amado",
        "vos": "habrás amado",
        "usted": "habrá amado",
        "él": "habrá amado",
        "ella": "habrá amado",
        "nosotros": "habremos amado",
        "nosotras": "habremos amado",
        "vosotros": "habréis amado",
        "vosotras": "habréis amado",
        "ustedes": "habrán amado",
        "ellos": "habrán amado",
        "ellas": "habrán amado",
    }

def test_indicative_conditional_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría amado",
        "tú": "habrías amado",
        "vos": "habrías amado",
        "usted": "habría amado",
        "él": "habría amado",
        "ella": "habría amado",
        "nosotros": "habríamos amado",
        "nosotras": "habríamos amado",
        "vosotros": "habríais amado",
        "vosotras": "habríais amado",
        "ustedes": "habrían amado",
        "ellos": "habrían amado",
        "ellas": "habrían amado",
    }

def test_subjunctive_present():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_present() == {
        "yo": "ame",
        "tú": "ames",
        "vos": "amés",
        "usted": "ame",
        "él": "ame",
        "ella": "ame",
        "nosotros": "amemos",
        "nosotras": "amemos",
        "vosotros": "améis",
        "vosotras": "améis",
        "ustedes": "amen",
        "ellos": "amen",
        "ellas": "amen",
    }

def test_subjunctive_imperfect_preterite():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_imperfect_preterite(alternate_form = False) == {
        "yo": "amara",
        "tú": "amaras",
        "vos": "amaras",
        "usted": "amara",
        "él": "amara",
        "ella": "amara",
        "nosotros": "amáramos",
        "nosotras": "amáramos",
        "vosotros": "amarais",
        "vosotras": "amarais",
        "ustedes": "amaran",
        "ellos": "amaran",
        "ellas": "amaran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_imperfect_preterite(alternate_form = True) == {
        "yo": "amase",
        "tú": "amases",
        "vos": "amases",
        "usted": "amase",
        "él": "amase",
        "ella": "amase",
        "nosotros": "amásemos",
        "nosotras": "amásemos",
        "vosotros": "amaseis",
        "vosotras": "amaseis",
        "ustedes": "amasen",
        "ellos": "amasen",
        "ellas": "amasen",
    }

def test_subjunctive_future():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_future() == {
        "yo": "amare",
        "tú": "amares",
        "vos": "amares",
        "usted": "amare",
        "él": "amare",
        "ella": "amare",
        "nosotros": "amáremos",
        "nosotras": "amáremos",
        "vosotros": "amareis",
        "vosotras": "amareis",
        "ustedes": "amaren",
        "ellos": "amaren",
        "ellas": "amaren",
    }

def test_subjunctive_present_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya amado",
        "tú": "hayas amado",
        "vos": "hayas amado",
        "usted": "haya amado",
        "él": "haya amado",
        "ella": "haya amado",
        "nosotros": "hayamos amado",
        "nosotras": "hayamos amado",
        "vosotros": "hayáis amado",
        "vosotras": "hayáis amado",
        "ustedes": "hayan amado",
        "ellos": "hayan amado",
        "ellas": "hayan amado",
    }

def test_subjunctive_past_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_past_perfect(alternate_form = False) == {
        "yo": "hubiera amado",
        "tú": "hubieras amado",
        "vos": "hubieras amado",
        "usted": "hubiera amado",
        "él": "hubiera amado",
        "ella": "hubiera amado",
        "nosotros": "hubiéramos amado",
        "nosotras": "hubiéramos amado",
        "vosotros": "hubierais amado",
        "vosotras": "hubierais amado",
        "ustedes": "hubieran amado",
        "ellos": "hubieran amado",
        "ellas": "hubieran amado",
    }

def test_subjunctive_past_perfect_alternate():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_past_perfect(alternate_form = True) == {
        "yo": "hubiese amado",
        "tú": "hubieses amado",
        "vos": "hubieses amado",
        "usted": "hubiese amado",
        "él": "hubiese amado",
        "ella": "hubiese amado",
        "nosotros": "hubiésemos amado",
        "nosotras": "hubiésemos amado",
        "vosotros": "hubieseis amado",
        "vosotras": "hubieseis amado",
        "ustedes": "hubiesen amado",
        "ellos": "hubiesen amado",
        "ellas": "hubiesen amado",
    }

def test_subjunctive_future_perfect():
    verb = RegularFirstGroup("amar")
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere amado",
        "tú": "hubieres amado",
        "vos": "hubieres amado",
        "usted": "hubiere amado",
        "él": "hubiere amado",
        "ella": "hubiere amado",
        "nosotros": "hubiéremos amado",
        "nosotras": "hubiéremos amado",
        "vosotros": "hubiereis amado",
        "vosotras": "hubiereis amado",
        "ustedes": "hubieren amado",
        "ellos": "hubieren amado",
        "ellas": "hubieren amado",
    }

def test_imperative_affirmative():
    verb = RegularFirstGroup("amar")
    assert verb.imperative_affirmative() == {
        "tú": "ama",
        "vos": "amá",
        "usted": "ame",
        "nosotros": "amemos",
        "nosotras": "amemos",
        "vosotros": "amad",
        "vosotras": "amad",
        "ustedes": "amen",
    }

def test_imperative_negative():
    verb = RegularFirstGroup("amar")
    assert verb.imperative_negative() == {
        "tú": "ames",
        "vos": "amés",
        "usted": "ame",
        "nosotros": "amemos",
        "nosotras": "amemos",
        "vosotros": "améis",
        "vosotras": "améis",
        "ustedes": "amen",
    }
