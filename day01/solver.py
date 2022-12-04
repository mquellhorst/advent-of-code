with open("input.txt", "r") as f:
    elves = sorted(
        [sum([int(c) for c in elf.split("\n")]) for elf in f.read()[:-1].split("\n\n")],
        reverse=True
    )

print(f"Part 1: {elves[0]}")
print(f"Part 2: {sum(elves[:3])}")
