import itertools
from simpleai.search import CspProblem, backtrack

parejas = [
    ("AA", 1),
    ("BB", 1),
    ("CC", 2),
    ("DD", 2),
    ("FF", 2),
    ("GG", 2),
    ("HH", 3),
    ("JJ", 3),

]
CANTIDAD_GRUPOS = 4
TAM_GRUPOS = 2
combinaciones = list(itertools.combinations(parejas, TAM_GRUPOS))

combinaciones_filtradas = []
for c in combinaciones:
    elementos = set([e[0] for e in c])
    if len(elementos) == TAM_GRUPOS:
        combinaciones_filtradas.append(c)
variables = [f"Group {n}" for n in range(CANTIDAD_GRUPOS)]

domains = {
    group : combinaciones_filtradas
    for group in variables
}

def equal_values(variables, values):
    sum_a = sum([value_a[1] for value_a in values[1]])
    sum_b = sum([value_b[1] for value_b in values[0]])

    return sum_a == sum_b

def distinct(variables, values):
    set_a = set([value_a[0] for value_a in values[1]])
    set_b = set([value_b[0] for value_b in values[0]])
    set_all = set_a | set_b
    return len(set_all) == TAM_GRUPOS * 2

constraints = [
    (g, equal_values)
    for g in itertools.combinations(variables, 2)
] + [
    (g, distinct)
    for g in itertools.combinations(variables, 2)
]

problem = CspProblem(variables=variables, domains=domains, constraints=constraints)
groups = backtrack(problem)

print(groups)