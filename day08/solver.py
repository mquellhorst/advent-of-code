rows = open("input.txt", "r").read()[:-1].split("\n")
rows = [list(map(int, r)) for r in rows]

h = len(rows[0])
w = len(rows)

def is_visible(t, y, x):
    ucol = [rows[i][x] for i in range(0, y)]
    if t > max(ucol): return True
    bcol = [rows[i][x] for i in range(y + 1, h)]
    if t > max(bcol): return True
    lrow = [rows[y][i] for i in range(0, x)]
    if t > max(lrow): return True
    rrow = [rows[y][i] for i in range(x + 1, w)]
    if t > max(rrow): return True
    return False

def calc_scenic_score(t, y, x):
    tscore = 0
    tcol = reversed([rows[i][x] for i in range(0, y)])
    for st in tcol:
        tscore += 1
        if st >= t:
            break
    bscore = 0
    bcol = [rows[i][x] for i in range(y + 1, h)]
    for st in bcol:
        bscore += 1
        if st >= t:
            break
    lscore = 0
    lrow = reversed([rows[y][i] for i in range(0, x)])
    for st in lrow:
        lscore += 1
        if st >= t:
            break
    rscore = 0
    rrow = [rows[y][i] for i in range(x + 1, w)]
    for st in rrow:
        rscore += 1
        if st >= t:
            break
    return tscore * bscore * lscore * rscore

highest_score = 0
visible = (w * 2 + h * 2) - 4
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if is_visible(rows[i][j], i, j):
            visible += 1
        score = calc_scenic_score(rows[i][j], i, j)
        if score > highest_score: highest_score = score

print(f"Part 1: {visible}")
print(f"Part 2: {highest_score}")
