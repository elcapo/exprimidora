from exprimidora import RegularThirdGroup

def test_root_participle_and_gerund():
    verb = RegularThirdGroup("vivir")
    assert verb.root() == "viv"
    assert verb.gerund() == "viviendo"
    assert verb.participle() == "vivido"

def test_indicative_present():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_present() == {
        "yo": "vivo",
        "tú": "vives",
        "vos": "vivís",
        "usted": "vive",
        "él": "vive",
        "ella": "vive",
        "nosotros": "vivimos",
        "nosotras": "vivimos",
        "vosotros": "vivís",
        "vosotras": "vivís",
        "ustedes": "viven",
        "ellos": "viven",
        "ellas": "viven",
    }

def test_indicative_imperfect():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_imperfect() == {
        "yo": "vivía",
        "tú": "vivías",
        "vos": "vivías",
        "usted": "vivía",
        "él": "vivía",
        "ella": "vivía",
        "nosotros": "vivíamos",
        "nosotras": "vivíamos",
        "vosotros": "vivíais",
        "vosotras": "vivíais",
        "ustedes": "vivían",
        "ellos": "vivían",
        "ellas": "vivían",
    }

def test_indicative_preterite():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_preterite() == {
        "yo": "viví",
        "tú": "viviste",
        "vos": "viviste",
        "usted": "vivió",
        "él": "vivió",
        "ella": "vivió",
        "nosotros": "vivimos",
        "nosotras": "vivimos",
        "vosotros": "vivisteis",
        "vosotras": "vivisteis",
        "ustedes": "vivieron",
        "ellos": "vivieron",
        "ellas": "vivieron",
    }

def test_indicative_future():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_future() == {
        "yo": "viviré",
        "tú": "vivirás",
        "vos": "vivirás",
        "usted": "vivirá",
        "él": "vivirá",
        "ella": "vivirá",
        "nosotros": "viviremos",
        "nosotras": "viviréis",
        "vosotros": "viviréis",
        "vosotras": "viviréis",
        "ustedes": "vivirán",
        "ellos": "vivirán",
        "ellas": "vivirán",
    }

def test_indicative_conditional():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_conditional() == {
        "yo": "viviría",
        "tú": "vivirías",
        "vos": "vivirías",
        "usted": "viviría",
        "él": "viviría",
        "ella": "viviría",
        "nosotros": "viviríamos",
        "nosotras": "viviríamos",
        "vosotros": "viviríais",
        "vosotras": "viviríais",
        "ustedes": "vivirían",
        "ellos": "vivirían",
        "ellas": "vivirían",
    }

def test_indicative_present_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_present_perfect() == {
        "yo": "he vivido",
        "tú": "has vivido",
        "vos": "has vivido",
        "usted": "ha vivido",
        "él": "ha vivido",
        "ella": "ha vivido",
        "nosotros": "hemos vivido",
        "nosotras": "hemos vivido",
        "vosotros": "habéis vivido",
        "vosotras": "habéis vivido",
        "ustedes": "han vivido",
        "ellos": "han vivido",
        "ellas": "han vivido",
    }

def test_indicative_past_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_past_perfect() == {
        "yo": "había vivido",
        "tú": "habías vivido",
        "vos": "habías vivido",
        "usted": "había vivido",
        "él": "había vivido",
        "ella": "había vivido",
        "nosotros": "habíamos vivido",
        "nosotras": "habíamos vivido",
        "vosotros": "habíais vivido",
        "vosotras": "habíais vivido",
        "ustedes": "habían vivido",
        "ellos": "habían vivido",
        "ellas": "habían vivido",
    }

def test_indicative_past_anterior():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_past_anterior() == {
        "yo": "hube vivido",
        "tú": "hubiste vivido",
        "vos": "hubiste vivido",
        "usted": "hubo vivido",
        "él": "hubo vivido",
        "ella": "hubo vivido",
        "nosotros": "hubimos vivido",
        "nosotras": "hubimos vivido",
        "vosotros": "hubisteis vivido",
        "vosotras": "hubisteis vivido",
        "ustedes": "hubieron vivido",
        "ellos": "hubieron vivido",
        "ellas": "hubieron vivido",
    }

def test_indicative_future_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_future_perfect() == {
        "yo": "habré vivido",
        "tú": "habrás vivido",
        "vos": "habrás vivido",
        "usted": "habrá vivido",
        "él": "habrá vivido",
        "ella": "habrá vivido",
        "nosotros": "habremos vivido",
        "nosotras": "habremos vivido",
        "vosotros": "habréis vivido",
        "vosotras": "habréis vivido",
        "ustedes": "habrán vivido",
        "ellos": "habrán vivido",
        "ellas": "habrán vivido",
    }

def test_indicative_conditional_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.indicative_conditional_perfect() == {
        "yo": "habría vivido",
        "tú": "habrías vivido",
        "vos": "habrías vivido",
        "usted": "habría vivido",
        "él": "habría vivido",
        "ella": "habría vivido",
        "nosotros": "habríamos vivido",
        "nosotras": "habríamos vivido",
        "vosotros": "habríais vivido",
        "vosotras": "habríais vivido",
        "ustedes": "habrían vivido",
        "ellos": "habrían vivido",
        "ellas": "habrían vivido",
    }

def test_subjunctive_present():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_present() == {
        "yo": "viva",
        "tú": "vivas",
        "vos": "vivás",
        "usted": "viva",
        "él": "viva",
        "ella": "viva",
        "nosotros": "vivamos",
        "nosotras": "vivamos",
        "vosotros": "viváis",
        "vosotras": "viváis",
        "ustedes": "vivan",
        "ellos": "vivan",
        "ellas": "vivan",
    }

def test_subjunctive_imperfect_preterite():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_imperfect_preterite(alternate_form = False) == {
        "yo": "viviera",
        "tú": "vivieras",
        "vos": "vivieras",
        "usted": "viviera",
        "él": "viviera",
        "ella": "viviera",
        "nosotros": "viviéramos",
        "nosotras": "viviéramos",
        "vosotros": "vivierais",
        "vosotras": "vivierais",
        "ustedes": "vivieran",
        "ellos": "vivieran",
        "ellas": "vivieran",
    }

def test_subjunctive_imperfect_preterite_alternate():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_imperfect_preterite(alternate_form = True) == {
        "yo": "viviese",
        "tú": "vivieses",
        "vos": "vivieses",
        "usted": "viviese",
        "él": "viviese",
        "ella": "viviese",
        "nosotros": "viviésemos",
        "nosotras": "viviésemos",
        "vosotros": "vivieseis",
        "vosotras": "vivieseis",
        "ustedes": "viviesen",
        "ellos": "viviesen",
        "ellas": "viviesen",
    }

def test_subjunctive_future():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_future() == {
        "yo": "viviere",
        "tú": "vivieres",
        "vos": "vivieres",
        "usted": "viviere",
        "él": "viviere",
        "ella": "viviere",
        "nosotros": "viviéremos",
        "nosotras": "viviéremos",
        "vosotros": "viviereis",
        "vosotras": "viviereis",
        "ustedes": "vivieren",
        "ellos": "vivieren",
        "ellas": "vivieren",
    }

def test_subjunctive_present_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_present_perfect() == {
        "yo": "haya vivido",
        "tú": "hayas vivido",
        "vos": "hayas vivido",
        "usted": "haya vivido",
        "él": "haya vivido",
        "ella": "haya vivido",
        "nosotros": "hayamos vivido",
        "nosotras": "hayamos vivido",
        "vosotros": "hayáis vivido",
        "vosotras": "hayáis vivido",
        "ustedes": "hayan vivido",
        "ellos": "hayan vivido",
        "ellas": "hayan vivido",
    }

def test_subjunctive_past_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_past_perfect(alternate_form = False) == {
        "yo": "hubiera vivido",
        "tú": "hubieras vivido",
        "vos": "hubieras vivido",
        "usted": "hubiera vivido",
        "él": "hubiera vivido",
        "ella": "hubiera vivido",
        "nosotros": "hubiéramos vivido",
        "nosotras": "hubiéramos vivido",
        "vosotros": "hubierais vivido",
        "vosotras": "hubierais vivido",
        "ustedes": "hubieran vivido",
        "ellos": "hubieran vivido",
        "ellas": "hubieran vivido",
    }

def test_subjunctive_past_perfect_alternate():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_past_perfect(alternate_form = True) == {
        "yo": "hubiese vivido",
        "tú": "hubieses vivido",
        "vos": "hubieses vivido",
        "usted": "hubiese vivido",
        "él": "hubiese vivido",
        "ella": "hubiese vivido",
        "nosotros": "hubiésemos vivido",
        "nosotras": "hubiésemos vivido",
        "vosotros": "hubieseis vivido",
        "vosotras": "hubieseis vivido",
        "ustedes": "hubiesen vivido",
        "ellos": "hubiesen vivido",
        "ellas": "hubiesen vivido",
    }

def test_subjunctive_future_perfect():
    verb = RegularThirdGroup("vivir")
    assert verb.subjunctive_future_perfect() == {
        "yo": "hubiere vivido",
        "tú": "hubieres vivido",
        "vos": "hubieres vivido",
        "usted": "hubiere vivido",
        "él": "hubiere vivido",
        "ella": "hubiere vivido",
        "nosotros": "hubiéremos vivido",
        "nosotras": "hubiéremos vivido",
        "vosotros": "hubiereis vivido",
        "vosotras": "hubiereis vivido",
        "ustedes": "hubieren vivido",
        "ellos": "hubieren vivido",
        "ellas": "hubieren vivido",
    }

def test_imperative_affirmative():
    verb = RegularThirdGroup("vivir")
    assert verb.imperative_affirmative() == {
        "tú": "vive",
        "vos": "viví",
        "usted": "viva",
        "nosotros": "vivamos",
        "nosotras": "vivamos",
        "vosotros": "vivid",
        "vosotras": "vivid",
        "ustedes": "vivan",
    }

def test_imperative_negative():
    verb = RegularThirdGroup("vivir")
    assert verb.imperative_negative() == {
        "tú": "vivas",
        "vos": "vivás",
        "usted": "viva",
        "nosotros": "vivamos",
        "nosotras": "vivamos",
        "vosotros": "viváis",
        "vosotras": "viváis",
        "ustedes": "vivan",
    }
