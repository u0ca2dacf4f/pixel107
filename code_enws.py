"""Quick helpers."""

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(clamp(8, 0, 19))
