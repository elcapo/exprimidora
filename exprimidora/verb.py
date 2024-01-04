from typing import Union
from exprimidora import BaseVerb

class Verb(BaseVerb):
    def __init__(self, infinitive: str):
        super().__init__()
        self.infinitive = infinitive
