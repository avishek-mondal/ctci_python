def is_unique(inp:str):
    s = set()
    for ch in inp:
        if ch in s:
            return False
        s.add(ch)
    return True


def main():
    unique_str = "".join([chr(val) for val in range(128)])
    print(is_unique(unique_str))