from exprimidora.verb import Verb
from typing import Union

class IrregularToHave(Verb):
    def __init__(self):
        self.to_have = self
        self.infinitive = "haber"

    def gerund(self) -> str:
        return "habiendo"

    def participle(self) -> str:
        return "habido"

    def indicative_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_imperfect(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_preterite(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def indicative_conditional(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_present(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_imperfect_preterite(self, person: str = None, alternate_form: bool = False) -> Union[dict, str]:
        if not alternate_form:
            conjugation = {
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
        else:
            conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def subjunctive_future(self, person: str = None) -> Union[dict, str]:
        conjugation = {
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

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_affirmative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "he",
            "vos": "he",
            "usted": "haya",
            "nosotros": "hayamos",
            "nosotras": "hayamos",
            "vosotros": "habed",
            "vosotras": "habed",
            "ustedes": "hayan",
        }

        if person:
            return conjugation[person]
        
        return conjugation

    def imperative_negative(self, person: str = None) -> Union[dict, str]:
        conjugation = {
            "tú": "hayas",
            "vos": "hayás",
            "usted": "haya",
            "nosotros": "hayamos",
            "nosotras": "hayamos",
            "vosotros": "hayáis",
            "vosotras": "hayáis",
            "ustedes": "hayan",
        }

        if person:
            return conjugation[person]
        
        return conjugation
