from knowledge_base import KnowledgeBase
from solver import Solver


def do_check(rules, init_facts, queries,
             test_name):  # ['A', ['B', 'C']], ['A', 'B', 'C'], {'A': True, 'B': True, 'C': True}
    print(f'Test {test_name}')
    kb = KnowledgeBase()
    for rule in rules:
        kb.add_knowledge(rule[0], rule[1])
    for i_f in init_facts:
        kb.set_fact_state(i_f)
    s = Solver(kb)
    res = dict()
    print(f'Init Facts: {init_facts}')
    for q, val in queries.items():
        # print(f" Fact {q} is {s.solve_fact(q)}")
        res[q] = s.solve_fact(q)

    print(f'Expected {queries}\n     Got {res}')

    assert queries == res


def test_and():
    test_name = 'AND'
    a = ['A', list('B')]
    b = ['B', list('DE+')]
    f = ['F', list('GH+')]
    g = ['G', list('IJ+')]
    h = ['H', list('G')]
    k = ['K', list('LM+')]
    # O + P => L + N
    l = ['L', list('OP+')]
    n = ['N', list('OP+')]

    m = ['M', list('N')]
    d = ['D', None]
    e = ['E', None]
    i = ['I', None]
    j = ['J', None]
    o = ['O', None]
    p = ['P', None]

    rules = [a, b, f, g, h, k, l, n, m, d, e, i, j, o, p]

    init_facts = ['D', 'E', 'I', 'J', 'O', 'P']

    queries = {'A': True, 'F': True, 'K': True, 'P': True}

    do_check(rules, init_facts, queries, test_name)

    init_facts2 = ['D', 'E', 'I', 'J', 'P']
    queries2 = {'A': True, 'F': True, 'K': False, 'P': True}

    do_check(rules, init_facts2, queries2, test_name)


def test_or():
    test_name = 'OR'
    a = ['A', list('BC+')]
    b = ['B', list('DE|')]
    c = ['C', list('B')]
    d = ['D', None]
    e = ['E', None]

    rules = [a, b, c, d, e]
    init_facts = []
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['D']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['E']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['D', 'E']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)


def test_xor():
    test_name = 'XOR'
    a = ['A', list('BC+')]
    b = ['B', list('DE^')]
    c = ['C', list('B')]
    d = ['D', None]
    e = ['E', None]

    rules = [a, b, c, d, e]
    init_facts = []
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['D']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['E']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['D', 'E']
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)


def test_negation():
    test_name = 'NEGATION'
    a = ['A', list('BC!+')]
    b = ['B', None]
    c = ['C', None]

    rules = [a, b, c]
    init_facts = []
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['B']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['C']
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['B', 'C']
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)


def test_same_conclusion_multiple_rules():
    test_name = 'same_conclusion_multiple_rules'
    a = ['A', list('B')]
    a2 = ['A', list('C')]
    b = ['B', None]
    c = ['C', None]

    rules = [a, a2, b, c]
    init_facts = []
    queries = {'A': False}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['B']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['C']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)
    init_facts = ['B', 'C']
    queries = {'A': True}
    do_check(rules, init_facts, queries, test_name)


def test_parentheses():
    test_name = 'parentheses'
    e = ['E', list('BC+A|')]
    e2 = ['E', list('FG|H+')]
    a = ['A', None]
    b = ['B', None]
    c = ['C', None]
    f = ['F', None]
    g = ['G', None]
    h = ['H', None]

    rules = [a, b, c, f, g, h, e, e2]
    init_facts = []
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['A']
    queries = {'E': True}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['B']
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['C']
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['A', 'C']
    queries = {'E': True}  # TODO in corrections is False
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['B', 'C']
    queries = {'E': True}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['F']
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['G']
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['H']
    queries = {'E': False}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['F', 'H']
    queries = {'E': True}
    do_check(rules, init_facts, queries, test_name)

    init_facts = ['G', 'H']
    queries = {'E': True}
    do_check(rules, init_facts, queries, test_name)


if __name__ == '__main__':
    test_parentheses()
