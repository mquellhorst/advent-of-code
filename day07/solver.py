lns = open("input.txt", "r").read()[:-1].split("\n")

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def size(self):
        s = 0
        for c in self.children:
            s += c.size()
        for f in self.files:
            s += f
        return s

root = Dir("root", None)
pwd = None
for l in lns:
    if l.startswith("$"):
        if l.startswith("$ cd"):
            cmd_dir = l.split(" ")[2]
            if cmd_dir == "/":
                pwd = root
            elif cmd_dir == "..":
                pwd = pwd.parent
            else:
                pwd = next(filter(lambda d: d.name == cmd_dir, pwd.children), None)
    elif l.startswith("dir"):
        pwd.children.append(Dir(l.split(" ")[1], pwd))
    else:
        file_size = int(l.split(" ")[0])
        pwd.files.append(file_size)

print(root.size())

total_size = 0
size_needed = abs(70000000 - 30000000 - root.size())
smallest_dir = root.size()
def check_size(dir, part):
    global total_size
    global smallest_dir
    size = dir.size()
    if part == 1:
        if size < 100000:
            total_size += size
    if part == 2:
        if size >= size_needed:
            if size < smallest_dir:
                smallest_dir = size


def walk_tree(dir, part):
    for directory in dir.children:
        check_size(directory, part)
        walk_tree(directory, part)

check_size(root, 1)
walk_tree(root, 1)

print(f"Part 1: {total_size}")

walk_tree(root, 2)

print(f"Part 2: {smallest_dir}")
