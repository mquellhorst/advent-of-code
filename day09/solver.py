
tp = []
h = [0, 0]
t = [0, 0]

def calc_move(direction):
    global tp, h, t
    match direction:
        case "U":
            h[1] += 1
            if t[1] + 1 < h[1]:
                t[1] = h[1] - 1
                if t[0] != h[0]:
                    t[0] = h[0]
        case "D":
            h[1] -= 1
            if t[1] > h[1] + 1:
                t[1] = h[1] + 1
                if t[0] != h[0]:
                    t[0] = h[0]
        case "L":
            h[0] -= 1
            if t[0] > h[0] + 1:
                t[0] = h[0] + 1
                if t[1] != h[1]:
                    t[1] = h[1]
        case "R":
            h[0] += 1
            if t[0] + 1 < h[0]:
                t[0] = h[0] - 1
                if t[1] != h[1]:
                    t[1] = h[1]
    tp.append(t)

for l in f:
    move = l.split(" ")
    move[1] = int(move[1])
    i = 0
    while i < move[1]:
        calc_move(move[0])
        i += 1

print(tp)
print(f"Part 1: {len(tp)}")

def parse_input(filename):
    with open(filename, "r") as f:
        return [
            (d, int(m)) for (d, m) in [l.strip().split(' ') in f.readlines()]
        ]

if __name__ == "__main__":
    input_path = "./input.txt"
    print(parse_input(input_path))
