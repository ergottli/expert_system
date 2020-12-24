def bin_operation_wrapper(func):
    def wrapped_operation(operators):
        return func(operators[0], operators[1])

    return wrapped_operation


def and_operation(left, right):
    return left and right


def or_operation(left, right):
    return left or right


def xor_operation(left, right):
    return left ^ right


def not_operation(operands):
    return not operands[0]


OPERATIONS = {'+': bin_operation_wrapper(and_operation),
              '|': bin_operation_wrapper(or_operation),
              '^': bin_operation_wrapper(xor_operation),
              '!': not_operation}
