from expert_system import ExpertSystem
import os
import pathlib
from termcolor import cprint

DIRECTORY = pathlib.Path(__file__).parent.absolute()

FILES = {
    'AND_1': [os.path.join(DIRECTORY, "examples/test/and_1"), {'A': True, 'F': True, 'K': True, 'P': True}],
    'AND_2': [os.path.join(DIRECTORY, "examples/test/and_2"), {'A': True, 'F': True, 'K': False, 'P': True}],
    'OR_1': [os.path.join(DIRECTORY, "examples/test/or_1"), {'A': False}],
    'OR_2': [os.path.join(DIRECTORY, "examples/test/or_2"), {'A': True}],
    'OR_3': [os.path.join(DIRECTORY, "examples/test/or_3"), {'A': True}],
    'OR_4': [os.path.join(DIRECTORY, "examples/test/or_4"), {'A': True}],
    'XOR_1': [os.path.join(DIRECTORY, "examples/test/xor_1"), {'A': False}],
    'XOR_2': [os.path.join(DIRECTORY, "examples/test/xor_2"), {'A': True}],
    'XOR_3': [os.path.join(DIRECTORY, "examples/test/xor_3"), {'A': True}],
    'XOR_4': [os.path.join(DIRECTORY, "examples/test/xor_4"), {'A': False}],
    'NEG_1': [os.path.join(DIRECTORY, "examples/test/neg_1"), {'A': False}],
    'NEG_2': [os.path.join(DIRECTORY, "examples/test/neg_2"), {'A': True}],
    'NEG_3': [os.path.join(DIRECTORY, "examples/test/neg_3"), {'A': False}],
    'NEG_4': [os.path.join(DIRECTORY, "examples/test/neg_4"), {'A': False}],
    'SCMR_1': [os.path.join(DIRECTORY, "examples/test/scmr_1"), {'A': False}],  # Same conclusion in multiple rules
    'SCMR_2': [os.path.join(DIRECTORY, "examples/test/scmr_2"), {'A': True}],
    'SCMR_3': [os.path.join(DIRECTORY, "examples/test/scmr_3"), {'A': True}],
    'SCMR_4': [os.path.join(DIRECTORY, "examples/test/scmr_4"), {'A': True}],
    'PAR_1': [os.path.join(DIRECTORY, "examples/test/parentheses_1"), {'E': False}],
    'PAR_2': [os.path.join(DIRECTORY, "examples/test/parentheses_2"), {'E': True}],
    'PAR_3': [os.path.join(DIRECTORY, "examples/test/parentheses_3"), {'E': False}],
    'PAR_4': [os.path.join(DIRECTORY, "examples/test/parentheses_4"), {'E': False}],
    'PAR_5': [os.path.join(DIRECTORY, "examples/test/parentheses_5"), {'E': True}],
    'PAR_6': [os.path.join(DIRECTORY, "examples/test/parentheses_6"), {'E': True}],
    'PAR_7': [os.path.join(DIRECTORY, "examples/test/parentheses_7"), {'E': False}],
    'PAR_8': [os.path.join(DIRECTORY, "examples/test/parentheses_8"), {'E': False}],
    'PAR_9': [os.path.join(DIRECTORY, "examples/test/parentheses_9"), {'E': False}],
    'PAR_10': [os.path.join(DIRECTORY, "examples/test/parentheses_10"), {'E': True}],
    'PAR_11': [os.path.join(DIRECTORY, "examples/test/parentheses_11"), {'E': True}],

}


def print_result(expected, result, text_test_name):
    cprint(text_test_name, "green")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")


def do_full_test(test_name):
    es = ExpertSystem(FILES[test_name][0])
    es.solve_queries()
    assert es.result == FILES[test_name][1]
    print_result(FILES[test_name][1], es.result, f"FULL_TEST: {test_name}")


def test_and_1():
    do_full_test('AND_1')


def test_and_2():
    do_full_test('AND_2')


def test_or_1():
    do_full_test('OR_1')


def test_or_2():
    do_full_test('OR_2')


def test_or_3():
    do_full_test('OR_3')


def test_or_4():
    do_full_test('OR_4')


def test_xor_1():
    do_full_test('XOR_1')


def test_xor_2():
    do_full_test('XOR_2')


def test_xor_3():
    do_full_test('XOR_3')


def test_xor_4():
    do_full_test('XOR_4')


def test_neg_1():
    do_full_test('NEG_1')


def test_neg_2():
    do_full_test('NEG_2')


def test_neg_3():
    do_full_test('NEG_3')


def test_neg_4():
    do_full_test('NEG_4')


def test_scmr_1():
    do_full_test('SCMR_1')


def test_scmr_2():
    do_full_test('SCMR_2')


def test_scmr_3():
    do_full_test('SCMR_3')


def test_scmr_4():
    do_full_test('SCMR_4')


def test_parentheses_1():
    do_full_test('PAR_1')


def test_parentheses_2():
    do_full_test('PAR_2')


def test_parentheses_3():
    do_full_test('PAR_3')


def test_parentheses_4():
    do_full_test('PAR_4')


def test_parentheses_5():
    do_full_test('PAR_5')


def test_parentheses_6():
    do_full_test('PAR_6')


def test_parentheses_7():
    do_full_test('PAR_7')


def test_parentheses_8():
    do_full_test('PAR_8')


def test_parentheses_9():
    do_full_test('PAR_9')


def test_parentheses_10():
    do_full_test('PAR_10')


def test_parentheses_11():
    do_full_test('PAR_11')


if __name__ == '__main__':
    test_and_1()
    test_and_2()
    test_or_1()
    test_or_2()
    test_or_3()
    test_or_4()
    test_xor_1()
    test_xor_2()
    test_xor_3()
    test_xor_4()
    test_neg_1()
    test_neg_2()
    test_neg_3()
    test_neg_4()
    test_parentheses_1()
    test_parentheses_2()
    test_parentheses_3()
    test_parentheses_4()
    test_parentheses_5()
    test_parentheses_6()
    test_parentheses_7()
    test_parentheses_8()
    test_parentheses_9()
    test_parentheses_10()
    test_parentheses_11()
