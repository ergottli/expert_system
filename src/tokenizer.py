import sys

from config import IMPLICATION_SYMBOL
from pythonds.basic import Stack


def create_postfix_notation(infixexpr):
    prec = {"!": 5, "+": 4, "|": 3, "^": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr.replace(" ", ""))
    tokens = []

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfixList.append(token)
            tokens.append(token)  # Запоминаем факты
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList, tokens


def tokenize_rules(rules):
    result = {}
    for rule in rules:
        split_rule = rule.split(IMPLICATION_SYMBOL)
        if split_rule[1].replace(" ", "") == 'F':
            pass
        operations, tokens = create_postfix_notation(split_rule[0])
        for t in split_rule[1].replace(" ", ""):
            if t in result.keys():
                result[t].append(operations)
            else:
                result[t] = [operations]
        for t in tokens:
            if not t in result.keys():
                result[t] = []
    return result


def validate_facts(init_facts, facts):
    for fact in init_facts:
        if fact not in facts:
            return fact
    return False


def tokenizer(rules, init_facts, query_facts):
    facts = tokenize_rules(rules)
    fact_check = validate_facts(init_facts, facts)
    if fact_check:
        print(f'initial fact is not in rules. fact: {fact_check}')
        sys.exit(0)
    fact_check = validate_facts(facts, facts)
    if fact_check:
        print(f'Query fact is not in rules. fact: {fact_check}')
        sys.exit(0)
    return facts, init_facts, query_facts
