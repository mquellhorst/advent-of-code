points = {
    "A": {
        "A": 1 + 3,
        "B": 2 + 6,
        "C": 3 + 0,
    },
    "B": {
        "A": 1 + 0,
        "B": 2 + 3,
        "C": 3 + 6,
    },
    "C": {
        "A": 1 + 6,
        "B": 2 + 0,
        "C": 3 + 3,
    },
}
gs = open("input.txt", "r").read()[:-1].split("\n")
trans = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}
ref = list(trans.values())

s = 0
for g in gs:
    o, m = g.split(" ")
    s += points[o][trans.get(m)]
print(f"Part 1: {s}")

s = 0
for g in gs:
    o, r = g.split(" ")
    if r == "X":
        s += points[o][ref[ref.index(o) - 1]]
    if r == "Y":
        s += points[o][o]
    if r == "Z":
        s += points[o][ref[(ref.index(o) + 1) % 3]]
print(f"Part 2: {s}")
