from exprimidora.irregular_to_have import IrregularToHave
from exprimidora.verb import Verb

class IrregularToBe(Verb):
    def __init__(self):
        self.to_have = IrregularToHave()
        self.infinitive = "ser"

    def gerund(self) -> str:
        return "siendo"

    def participle(self) -> str:
        return "sido"

    def indicative_present(self) -> dict:
        return {
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

    def indicative_imperfect(self) -> dict:
        return {
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

    def indicative_preterite(self) -> dict:
        return {
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

    def indicative_future(self) -> dict:
        return {
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

    def indicative_conditional(self) -> dict:
        return {
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

    def subjunctive_present(self) -> dict:
        return {
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

    def subjunctive_imperfect_preterite(self, alternate_form: bool = False) -> dict:
        if not alternate_form:
            return {
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
        else:
            return {
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

    def subjunctive_future(self) -> dict:
        return {
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

    def imperative_affirmative(self) -> dict:
        return {
            "tú": "sé",
            "vos": "sé",
            "usted": "sea",
            "nosotros": "seamos",
            "nosotras": "seamos",
            "vosotros": "sed",
            "vosotras": "sed",
            "ustedes": "sean",
        }

    def imperative_negative(self) -> dict:
        return {
            "tú": "seas",
            "vos": "seás",
            "usted": "sea",
            "nosotros": "seamos",
            "nosotras": "seamos",
            "vosotros": "seáis",
            "vosotras": "seáis",
            "ustedes": "sean",
        }
