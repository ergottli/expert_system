class Node:
    def __init__(self, name, rule):
        self.name = name
        self.rules = []
        self.add_rule(rule)
        self.state = False
        self.fact_state = False
        self.processed = False

    def add_rule(self, rule):
        if rule:
            self.rules.append(rule)

    def set_fact_state(self):
        self.fact_state = True

    def __str__(self):
        return f"Fact: {self.name} with rules: {self.rules} state: {self.state} fact_state: {self.fact_state}"


class KnowledgeBase:
    def __init__(self):
        self.knowledge_base = dict()

    def add_knowledge(self, name, rule):
        if name in self.knowledge_base:
            self.knowledge_base[name].add_rule(rule)
        else:
            self.knowledge_base[name] = Node(name, rule)

    def get_base(self):
        return self.knowledge_base.copy()

    def set_fact_state(self, name):
        self.knowledge_base[name].set_fact_state()

    def __str__(self):
        return "\n".join(list(map(str, self.knowledge_base.values())))
