from exprimidora import RegularThirdGroup

def test_list_all_simple_forms_flattened():
    verb = RegularThirdGroup("exprimir")
    assert verb.all_forms_flattened(only_simple = True) == [
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
        "exprimíamos", "exprimían", "exprimías", "exprimís"
    ]

def test_list_all_forms_flattened():
    verb = RegularThirdGroup("exprimir")
    assert verb.all_forms_flattened(only_simple = False) == [
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
        "ha exprimido", "habremos exprimido", "habrá exprimido",
        "habrán exprimido", "habrás exprimido", "habré exprimido",
        "habréis exprimido", "habría exprimido", "habríais exprimido",
        "habríamos exprimido", "habrían exprimido", "habrías exprimido",
        "habéis exprimido", "había exprimido", "habíais exprimido",
        "habíamos exprimido", "habían exprimido", "habías exprimido",
        "han exprimido", "has exprimido", "haya exprimido",
        "hayamos exprimido", "hayan exprimido", "hayas exprimido",
        "hayáis exprimido", "he exprimido", "hemos exprimido",
        "hube exprimido", "hubiera exprimido", "hubierais exprimido",
        "hubieran exprimido", "hubieras exprimido", "hubiere exprimido",
        "hubiereis exprimido", "hubieren exprimido", "hubieres exprimido",
        "hubieron exprimido", "hubimos exprimido", "hubiste exprimido",
        "hubisteis exprimido", "hubiéramos exprimido",
        "hubiéremos exprimido", "hubo exprimido",
    ]
