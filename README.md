# Exprimidora

> Me llamo `exprimidora` porque **con·jugo**.

## Introduction

This Python package conjugates Spanish verbs from their infinitive form.

### Example: Full Tense Conjugation

This code:

```python
from exprimidora import RegularFirstGroup

verb = RegularFirstGroup("amar")
verb.indicative_past_perfect()
```

... would procude this output.

```json
{
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
    "ellas": "habían amado"
}
```

### Example: Specific Conjugation

By adding the pronoun of the subject, a string with the verb conjugated for that person and verbe tense would be returned (rather than a dictionary with the full conjugation):

```python
from exprimidora import RegularFirstGroup

verb = RegularFirstGroup("amar")
verb.indicative_past_perfect("ustedes")
```

... would procude this output.

```json
"habían amado"
```

## All Available Verb Tenses

The following verb tenses can be conjugated:

### Non Personal Forms

- **gerund** (*gerundio*): estudiando
- **participle** (*participio*): estudiado

### Indicative

#### Simple

- **indicative_present** (*presente*): estudio
- **indicative_imperfect** (*pretérito imperfecto*): estudiaba
- **indicative_preterite** (*pretérito perfecto*): estudié
- **indicative_future** (*futuro*): estudiaré
- **indicative_conditional** (*condicional*): estudiaría

#### Compound

- **indicative_present_perfect** (*pretérito perfecto*): he estudiado
- **indicative_past_perfect** (*pretérito pluscuamperfecto*): había estudiado
- **indicative_past_anterior** (*pretérito anterior*): hube estudiado
- **indicative_future_perfect** (*futuro perfecto*): habré estudiado
- **indicative_conditional_perfect** (*condicional perfecto*): habría estudiado

### Subjunctive

#### Simple

- **subjunctive_present** (*presente*): estudie
- **subjunctive_imperfect_preterite** (*pretérito imperfecto*): estudiara
- **subjunctive_imperfect_preterite_alternative** (*pretérito imperfecto*): estudiase
- **subjunctive_future** (*futuro*): estudiare

#### Compound

- **subjunctive_present_perfect** (*pretérito perfecto*): haya estudiado
- **subjunctive_past_perfect** (*pretérito pluscuamperfecto*): hubiera estudiado
- **subjunctive_past_perfect_alternative** (*pretérito pluscuamperfecto*): hubiese estudiado
- **subjunctive_future_perfect** (*futuro*): hubiere estudiado

### Imperative

- **imperative_affirmative** (*imperativo afirmativo*): estudia
- **imperative_negative** (*imperativo negativo*): *no* estudies

## All Forms

The `all_forms_flattened` method can be used to obtain all the forms of a verb as a list.

### Example: All Simple Forms

This line:

```python
verb.all_forms_flattened(only_simple = True)
```

... would generate this:

```json
[
    "exprima", "exprimamos", "expriman", "exprimas", "exprime",
    "exprimen", "exprimes", "exprimid", "exprimido", "exprimiendo",
    "exprimiera", "exprimierais", "exprimieran", "exprimieras",
    "exprimiere", "exprimiereis", "exprimieren", "exprimieres",
    "exprimieron", "exprimimos", "exprimiremos", "exprimirá",
    "exprimirán", "exprimirás", "exprimiré", "exprimiréis",
    "exprimiría", "exprimiríais", "exprimiríamos", "exprimirían",
    "exprimirías", "exprimiste", "exprimisteis", "exprimiéramos",
    "exprimiéremos", "exprimió", "exprimo", "exprimáis",
    "exprimás", "exprimí", "exprimía", "exprimíais",
    "exprimíamos", "exprimían", "exprimías", "exprimís",
]
```

## Limitations

These are current limitations of the current version:

- only two irregular verbs (*ser* and *haber*) can be conjugated.

Please, check the project issues and milestones for information about next releases.

## Dependencies

### Production

This project does not rely on any dependency a part from:

- Python ^3.9

... in order to be executed.

### Development

To contribute with its development (and to follow this instructions), you will also need:

- Poetry
- Git

## Usage

Until a first production release of package is published, the package will only be available via Git. To run it, you'll need to clone the repository:

```bash
# Clone the repository using Git
git clone https://github.com/elcapo/exprimidora.git

# Install it
cd exprimidora/
poetry install

# Open a Poetry shell
poetry shell

# Now you can open a Python intepreter
# ... and run the examples above
python
```

> [!NOTE]: The former warning means that this won't be published as a `pip` package until a version is considered to be sufficiently developed.
