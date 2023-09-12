"""
Usage: python3 simulator.py "5 6" "0 3" wait
                             H W   box  ^ wait for enter at each step
"""
import sys

_, dims, box_pos, *argv = sys.argv

H, W = map(int, dims.split())
box = tuple(map(int, box_pos.split()))

# print(H, W, flush=True)

query = input()
query = query.replace("?", "").replace(" ", "").strip()

print(query, file=sys.stderr)

grid = [["." for _ in range(W)] for _ in range(H)]

pos = (0, 0)
grid[pos[0]][pos[1]] = "#"

def pp():
    # return
    for i in range(H):
        for j in range(W):
            x = grid[i][j]
            if (i, j) == box:
                x = "B"
            if (i, j) == pos:
                x = "O"
            print(x, end="", file=sys.stderr)
        print(file=sys.stderr)
    if argv and argv[0] == "wait":
        input()

pp()

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for d in query:
    dr, dc = dirs[d]
    tr, tc = pos[0] + dr, pos[1] + dc

    print(d, file=sys.stderr)

    if (tr, tc) == box or tr < 0 or tr >= H or tc < 0 or tc >= W:
        continue

    pos = (tr, tc)
    grid[pos[0]][pos[1]] = "#"

    pp()

print(*pos, flush=True)
