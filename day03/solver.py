from string import ascii_letters

rss = open("input.txt", "r").read()[:-1].split("\n")

r = 0
for rs in rss:
    n = len(rs)
    if n % 2 == 0:
        a = rs[0:n//2]
        b = rs[n//2:]
    else:
        a = rs[0:n//2+1]
        b = rs[n//2+1:]
    b = "".join(set(b))
    for c in b:
        if c in a:
            r += ascii_letters.index(c) + 1
            a.replace(c, '')
print(f"Part 1: {r}")

r = 0
for i in range(0, len(rss)):
    rss[i] = "".join(set(rss[i]))
grps = [rss[g:g + 3] for g in range(0, len(rss), 3)]

for gr in grps:
    for x in gr[0]:
        if x in gr[1]:
            if x in gr[2]:
                r += ascii_letters.index(x) + 1
print(f"Part 2: {r}")
