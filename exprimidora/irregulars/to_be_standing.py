from exprimidora.irregulars.to_have import IrregularToHave
from exprimidora.verb import Verb
from typing import Union

class IrregularToBeStanding(Verb):
    def __init__(self):
        self.to_have = IrregularToHave()
        self.infinitive = "estar"

    def gerund(self) -> str:
        return "estando"

    def participle(self) -> str:
        return "estado"

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite_alternate(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "está",
            "vos": "está",
            "usted": "esté",
            "nosotros": "estemos",
            "nosotras": "estemos",
            "vosotros": "estad",
            "vosotras": "estad",
            "ustedes": "estén",
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "estés",
            "vos": "estés",
            "usted": "esté",
            "nosotros": "estemos",
            "nosotras": "estemos",
            "vosotros": "estéis",
            "vosotras": "estéis",
            "ustedes": "estén",
        }

        if person:
            return conjugation[person]
        
        return conjugation
