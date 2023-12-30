# Exprimidora

> Me llamo `exprimidora` porque **conjugo**.

## Introducción

Este paquete es un conjugador de verbos en español. Dada la forma infinitiva, genera las correspondientes formas verbales.

### Ejemplo

```python
from exprimidora import RegularFirstGroup

verb = RegularFirstGroup("amar")
verb.gerund() # amando
verb.participle() # amado
```
