# Exprimidora

> Me llamo `exprimidora` porque **con·jugo**.

## Introduction

This Python package conjugates Spanish verbs from their infinitive form.

### Example

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
