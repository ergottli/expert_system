from knowledge_base import KnowledgeBase
from solver import Solver

k = KnowledgeBase()

a = 'A'
a_rule = None

b = 'B'
b_rule = ['C', 'D', '^']

c = 'C'
c_rule = ['A', 'B', '+']
c_rule2 = ['A', 'D', '|']

d = 'D'
d_rule = None

k.add_knowledge(c, c_rule)
# k.add_knowledge(c, c_rule2)
k.add_knowledge(a, a_rule)
k.add_knowledge(b, b_rule)
k.add_knowledge(d, d_rule)

k.set_fact_state(a)
k.set_fact_state(b)

print(k)

s = Solver(k)

solve_fact = c

print(f"Fact {solve_fact} is {s.solve_fact(solve_fact)}")
