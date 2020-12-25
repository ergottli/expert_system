from .operations import OPERATIONS


class Solver:
    def __init__(self, knowledge_base):
        self.knowledge_base_carry = knowledge_base
        self.knowledge_base = None

    def solve_fact(self, fact):
        self.knowledge_base = self.knowledge_base_carry.get_base()
        return self._solve_fact(self.knowledge_base[fact])

    def _solve_fact(self, node):
        if isinstance(node, bool):  # Из функции solve_rule может прийти bool выражение из списка правил
            return node
        if node.fact_state is True:
            return True
        elif node.rules:
            return self._solve_rules(node.rules)
        else:
            return node.state

    def _solve_rules(self, rules):
        result_rules = []
        for rule in rules:
            result_rules.append(self._solve_rule(rule))
        return self._choice_correct_result(rules, result_rules)

    def _choice_correct_result(self, rules, result_rules):
        result = {True: set(), False: set()}
        # Определяем, какие результаты были получены от правил с подтвержденными фактами
        for rule, res_rule in zip(rules, result_rules):
            for r in rule:
                if r in self.knowledge_base_carry.fixed_facts:
                    result[True].add(res_rule)
                    continue
                result[False].add(res_rule)
        if result[True]:
            return self._get_result(result[True])
        else:
            return self._get_result(result[False])

    def _get_result(self, results):
        if len(results) == 1:
            return results.pop()
        else:
            return None

    def _solve_rule(self, rule):
        if len(rule) == 1:
            if isinstance(rule[0], bool):
                return rule[0]
            return self._solve_fact(self.knowledge_base[rule[0]])
        for i in range(len(rule)):
            if rule[i] in OPERATIONS.keys():
                operands, start_position = self._get_operands_and_operator(rule, i)
                rule = rule[:start_position] + [OPERATIONS[rule[i]](operands)] + rule[i + 1:]

                return self._solve_rule(rule)

    def _get_operands_and_operator(self, rule, i):
        operands = []
        start_position = i-2
        if rule[i] == '!':
            start_position = i - 1
        for counter in range(start_position, i):
            if isinstance(rule[counter], bool):
                operand = rule[counter]
            else:
                operand = self.knowledge_base[rule[counter]]
            operands.append(self._solve_fact(operand))

        return operands, start_position
