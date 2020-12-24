from knowledge_base import KnowledgeBase
from solver import Solver
from parser import parse_input
from tokenizer import tokenizer
from termcolor import cprint


class ExpertSystem:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.facts, self.init_facts, self.query_facts = tokenizer(*parse_input())
        self.enrich_knowledge_base(self.facts)
        self.set_init_facts_knowledge_base(self.init_facts)
        self.s = Solver(self.knowledge_base)
        self.result = {}

    def enrich_knowledge_base(self, facts: dict):
        for fact, rules in facts.items():
            self.knowledge_base.add_knowledge(fact, None)
            for rule in rules:
                self.knowledge_base.add_knowledge(fact, rule)

    def set_init_facts_knowledge_base(self, init_facts):
        for fact in init_facts:
            self.knowledge_base.set_fact_state(fact)

    def solve_queries(self):
        for q in self.query_facts:
            self.result[q] = self.s.solve_fact(q)

    def print_result(self):
        if not self.result:
            cprint("No result! Yu must solve first", "red")
        for q, res in self.result.items():
            if res is True:
                cprint(f"{q} is {res}", "green")
            else:
                cprint(f"{q} is {res}", "red")
