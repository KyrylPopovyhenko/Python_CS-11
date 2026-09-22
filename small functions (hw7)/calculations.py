def mean(*values):
    """Returns the mean value. Returns None if no values are provided"""
    return sum(values)/len(values) if values else None

def clamp(value, lower=0, upper=100):
    """Returns value clamped between lower and upper. Returns None if lower > upper."""
    return None if lower > upper else lower if value < lower else upper if value > upper else value

def weighted_sum(values, weights):
    """Returns the weighted sum. Returns None if lists are empty or have different lengths."""
    if not values or not weights or len(values) != len(weights):
        return None
    else:
        num = 0
        for i in range(len(values)):
            num += values[i] * weights[i]
        return num

def format_record(name, **fields):
    return f"{name} | {fields}"

def factorial(n):
    """Returns factorial n (calculates in recursive)""" 
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)

def factorial_loop(n):
    """Returns factorial n (calculates in loop)"""
    if n < 0:
        return None
    result = 1
    for i in range(n):
        result *= i + 1
    return result
