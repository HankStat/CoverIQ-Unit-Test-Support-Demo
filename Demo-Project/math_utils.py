def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def pad_number(x):
    """Pad a number with leading zeros to ensure it has at least 'length' digits."""
    return str(x).zfill(5)