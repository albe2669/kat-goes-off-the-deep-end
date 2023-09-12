from sys import stdin


def next_line():
    return tuple(int(x) for x in next(stdin).split())


def query(instructions):
    print(f"? {''.join(instructions)}", flush=True)
    return next_line()


def answer(r, c):
    print(f"! {r} {c}", flush=True)


LEFT, RIGHT, UP, DOWN = "<>^v"

H, W = next_line()

for r in range(H):
    instructions = [DOWN] * r + [RIGHT] * W

    nr, nc = query(instructions)

    if nc < W - 1:
        answer(r, nc + 1)
        break
    if nr < r:
        answer(nr + 1, 0)
        break
