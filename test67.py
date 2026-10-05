# small utilities, no deps

def clamp(value, low, high):
    return max(low, min(value, high))

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

# see notes
