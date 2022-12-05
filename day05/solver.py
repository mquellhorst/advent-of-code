f = open("input.txt", "r").read()[:-1].split("\n")
moves = []
rows = []
for l in f:
    if l and not l.startswith(" 1"):
        if l.startswith("move"):
            moves.append([int(m) for m in l.split(" ")[1::2]])
        else:
            rows.append(l[1::4])

ss = [[row[i] for row in rows[::-1] if row[i] != " "] for i in range(len(rows[0]))]

s1 = [s[:] for s in ss]
for m in moves:
    trns = s1[m[1] - 1][-m[0]:]
    s1[m[2] - 1] = s1[m[2] - 1] + trns[::-1]
    del s1[m[1] - 1][-m[0]:]
r1 = "".join([s[-1] for s in s1 if s])

for m in moves:
    ss[m[2] - 1] = ss[m[2] - 1] + ss[m[1] - 1][-m[0]:]
    del ss[m[1] - 1][-m[0]:]
r2 = "".join([s[-1] for s in ss if s])

print(f"Part 1: {r1}")
print(f"Part 2: {r2}")
