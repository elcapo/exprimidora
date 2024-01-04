from exprimidora.irregulars.to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

class IrregularToBeExisting(Verb):
    def __init__(self):
        self.to_have = IrregularToHave()
        self.infinitive = "ser"

    def gerund(self) -> str:
        return "siendo"

    def participle(self) -> str:
        return "sido"

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite_alternate(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "sé",
            "vos": "sé",
            "usted": "sea",
            "nosotros": "seamos",
            "nosotras": "seamos",
            "vosotros": "sed",
            "vosotras": "sed",
            "ustedes": "sean",
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "seas",
            "vos": "seás",
            "usted": "sea",
            "nosotros": "seamos",
            "nosotras": "seamos",
            "vosotros": "seáis",
            "vosotras": "seáis",
            "ustedes": "sean",
        }

        if person:
            return conjugation[person]
        
        return conjugation
