import argparse
import sys
from pythonds.basic import Stack
from config import COMMENT_SYMBOL, IMPLICATION_SYMBOL, INIT_FACTS_SYMBOL, QUERY_SYMBOL, ELEMENTS_DICT, \
    PERMISSIBLE_L_RULE, PERMISSIBLE_R_RULE, ENGLISH_UPPERCASE
from common import error_exit


def valid_sequence_in_file(last_indexes):
    if -1 in last_indexes:
        for i, ind in enumerate(last_indexes):
            if ind == -1:
                print(f"There is no: {ELEMENTS_DICT[i]}")
        sys.exit(0)
    if last_indexes != sorted(last_indexes):
        error_exit("Wrong sequence in file, must be rules->initial_facts->queries")


def valid_brackets(rule):
    stack = Stack()
    for symbol in list(rule.replace(" ", "")):
        if symbol == '(':
            stack.push(symbol)
        if symbol == ')':
            if stack.isEmpty():
                return 0
            else:
                stack.pop()
    if stack.isEmpty():
        return 1
    return 0


def valid_symbols(to_check, example):
    for elem in to_check:
        if elem not in example:
            return False
    return True


def valid_rules(rules):
    rule_tokens = []
    for rule in rules:
        if IMPLICATION_SYMBOL not in rule:
            error_exit(f'There is no implication symbol ({IMPLICATION_SYMBOL}) in rule: {rule}')
        split_rule = rule.split(IMPLICATION_SYMBOL)
        split_rule[0] = split_rule[0].replace(' ', '')
        split_rule[1] = split_rule[1].replace(' ', '')
        if len(split_rule) != 2:
            error_exit(f'Too much implication symbols ({IMPLICATION_SYMBOL}) in rule: {rule}. Must be one')
        if not valid_brackets(split_rule[0]) or not valid_brackets(split_rule[1]):
            error_exit(f"Wrong brackets in rule {rule}")
        if not valid_symbols(split_rule[0], PERMISSIBLE_L_RULE) or not valid_symbols(split_rule[1], PERMISSIBLE_R_RULE):
            error_exit(f"Wrong symbol in rule: {rule}")
        rule_tokens.append([split_rule[0], split_rule[1]])

    return rule_tokens


def valid_init_facts_queries(facts_list, example, name_of_facts):
    if len(facts_list) > 1:
        error_exit(f"Too much {name_of_facts} rows. Expected 1 Got {len(facts_list)}")
    facts = facts_list[0]
    if not valid_symbols(facts, example):
        error_exit(f"Invalid symbol in {name_of_facts}: {facts}")
    if name_of_facts == 'queries' and len(facts) < 1:
        error_exit(f"There is no queries")
    return facts


def parse_file(data):
    init_facts = []
    query_facts = []
    rules = []
    last_indexes = [-1, -1, -1]  # индексы последних встретившихся элементов [rules, init_f, query]
    for i, row in enumerate(data):
        row = row.split(COMMENT_SYMBOL)[0].strip()
        if len(row) < 1:
            continue
        if row[0] == INIT_FACTS_SYMBOL:
            init_facts.append(row[1:])  # обрезаем '=' в начал строки
            last_indexes[1] = i
        elif row[0] == QUERY_SYMBOL:
            query_facts.append(row[1:])  # обрезаем '?' в начал строки
            last_indexes[2] = i
        else:
            rules.append(row)
            last_indexes[0] = i

    valid_sequence_in_file(last_indexes)
    rules = valid_rules(rules)
    init_facts = valid_init_facts_queries(init_facts, ENGLISH_UPPERCASE, "init_facts")
    query_facts = valid_init_facts_queries(query_facts, ENGLISH_UPPERCASE, "queries")

    return rules, init_facts, query_facts


def parse_input():
    parser = argparse.ArgumentParser(description="expert_system 21-school Moscow")
    parser.add_argument('-v', help='visualizer', action='store_true')
    parser.add_argument('-i', help='interactive mode', action='store_true')
    parser.add_argument('file', help='input file', type=argparse.FileType('r'))

    args = parser.parse_args()
    data = args.file.readlines()
    rules, init_facts, query_facts = parse_file(data)
    return rules, init_facts, query_facts
