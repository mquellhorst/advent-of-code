def part_one(file_path: str) -> int:
    motions = parse_input(file_path)
    tail = head = (0, 0)
    tail_positions = {tail}
    for d, v in motions:
        for _ in range(v):
            mx, my = move(d)
            head = (head[0] + mx, head[1] + my)
            tail = reposition_tail(tail, head)
            tail_positions.add(tail)
    return len(tail_positions)

def part_two(file_path: str) -> int:
    motions = parse_input(file_path)
    knots = [(0,0) for _ in range(10)]
    tail_positions = {knots[-1]}
    for d, v in motions:
        for _ in range(v):
            mx, my = move(d)
            knots[0] = (knots[0][0] + mx, knots[0][1] + my)
            for i in range(1, 10):
                knots[i] = reposition_tail(knots[i], knots[i - 1])
            tail_positions.add(knots[-1])
    return len(tail_positions)

def move(direction: str) -> tuple[int, int]:
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    return moves[direction]

def reposition_tail(
                    tail: tuple[int, int],
                    head: tuple[int, int]
                   ) -> tuple[int, int]:
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        tail = (tail[0], tail[1])
    elif dx == 0:
        tail = (tail[0], tail[1] + dy/abs(dy))
    elif dy == 0:
        tail = (tail[0] + dx/abs(dx), tail[1])
    else:
        tail = (tail[0] + dx/abs(dx), tail[1] + dy/abs(dy))
    return tail

def parse_input(file_path: str) -> list[tuple[str, int]]:
    with open(file_path, "r") as f:
        return [
            (d, int(v)) for (d, v) in [l.strip().split(' ') for l in f.readlines()]
        ]

if __name__ == "__main__":
    input_path = "./input.txt"
    print(f"Part 1: {part_one(input_path)}")
    print(f"Part 2: {part_two(input_path)}")
