def _safe_operation(a, b, operation):
    try:
        return operation(a, b)
    except TypeError:
        return "Error: Invalid input. Please provide numbers."


def add(a, b):
    return _safe_operation(a, b, lambda a, b: a + b)


def subtract(a, b):
    return _safe_operation(a, b, lambda a, b: a - b)


def multiply(a, b):
    return _safe_operation(a, b, lambda a, b: a * b)
