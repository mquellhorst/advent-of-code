import re

f = open("input.txt", "r").read()[:-1].split("\n")

prs = [tuple(map(int, re.findall(r"\d+", l))) for l in f]

r = 0
for pr in prs:
    if ((pr[0] <= pr[2] and pr[1] >= pr[3]) 
        or (pr[0] >= pr[2] and pr[1] <= pr[3])):
        r += 1
print(f"Part 1: {r}")

r = 0
for pr in prs:
    if ((pr[0] <= pr[2] <= pr[1]) or (pr[2] <= pr[0] <= pr[3])):
        r += 1
print(f"Part 2: {r}")
