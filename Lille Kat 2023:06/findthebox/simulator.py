H, W = 6, 8
query = """
? v >>>> ^ <<<< ^ <<<< >>>> <<< >>> v <<< >>> v <<< >>> v <<< >>> v <<< >>> v <<< >>> v <<< < ^^^^^^
"""
query = query.replace("?", "").replace(" ", "").strip()

box = (0, 3)

print(query)

grid = [["." for _ in range(W)] for _ in range(H)]

pos = (0, 0)
grid[pos[0]][pos[1]] = "#"

def pp():
    for i in range(H):
        for j in range(W):
            x = grid[i][j]
            if (i, j) == box:
                x = "B"
            if (i, j) == pos:
                x = "O"
            print(x, end="")
        print()
    input()

pp()

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for d in query:
    dr, dc = dirs[d]
    tr, tc = pos[0] + dr, pos[1] + dc

    print(d)

    if (tr, tc) == box or tr < 0 or tr >= H or tc < 0 or tc >= W:
        continue

    pos = (tr, tc)
    grid[pos[0]][pos[1]] = "#"

    pp()

print(pos)
