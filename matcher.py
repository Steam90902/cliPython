def simple_match(a,b):
    
    matches = sum(1 for x, y in zip(a, b) if x == y)
    return matches / max(len(a), len(b))