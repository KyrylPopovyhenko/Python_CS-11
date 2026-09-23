def mean(*values):
    """Returns the mean value. Returns None if no values are provided"""
    return sum(values)/len(values) if values else None

def clamp(value, lower=0, upper=100):
    """Returns value clamped between lower and upper. Returns None if lower > upper."""
    return None if lower > upper else lower if value < lower else upper if value > upper else value
