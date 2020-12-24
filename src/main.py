from knowledge_base import KnowledgeBase
from solver import Solver
from parser import parse_input

if __name__ == "__main__":
    rules, init_facts, query_facts = parse_input()
    print(rules, init_facts, query_facts)
