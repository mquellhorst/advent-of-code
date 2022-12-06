f = open("input.txt", "r").read()

def find_marker(l) -> int:
    i = l - 1
    while i < len(f):
        m = f[i - l:i]
        if len(set(m)) == l:
            break
        i += 1
    return i

print(f"Part 1: {find_marker(4)}")
print(f"Part 2: {find_marker(14)}")
