from sys import stdin, stderr
from math import ceil


def next_line():
    return tuple(int(x) for x in next(stdin).split())


def query(instructions):
    print(f"? {''.join(instructions)}", flush=True)
    return next_line()


def answer(r, c):
    print(f"! {r} {c}", flush=True)


def mirror(instructions):
    mirrored = []
    for s in instructions:
        for ins in s:
            if ins == LEFT:
                mirrored.append(RIGHT)
            elif ins == RIGHT:
                mirrored.append(LEFT)
            else:
                mirrored.append(ins)
    return mirrored


LEFT, RIGHT, UP, DOWN = "<>^v"

H, W = next_line()



# Straight-forward for single-row case
if H == 1:
    tr, tc = query([RIGHT * W])
    answer(0, tc + 1)
    exit(0)

# Straight-forward for single-column case
if W == 1:
    tr, tc = query([DOWN * H])
    answer(tr + 1, 0)
    exit(0)
elif W == 2:
    tr, tc = query([DOWN * H])
    if tr == H - 1:
        tr, tc = query([RIGHT, DOWN * H])
        if tc == 0:
            answer(0, 1)
        else:
            answer(tr + 1, 1)
    else:
        answer(tr + 1, 0)
    exit(0)


w = ceil(W / 2)

# Handle edge case of box in being in the first row
handle_first_row = [DOWN, RIGHT * w, UP, LEFT * w, UP]


# Definition: "left side" includes middle column in odd-width rooms
CASE_LEFTMOST_COLUMN = 1
CASE_RIGHT_SIDE = 2
CASE_LEFT_SIDE = 3


def check_left_half():
    instructions = []
    instructions.extend(handle_first_row)

    s = W // 2

    # Go to the right side and go down. Then all the way left again, go back out.
    # If the box is in the left side, we will hit the box when going left in some row.
    for _ in range(H):
        instructions.append(LEFT * s)
        instructions.append(RIGHT * s)
        instructions.append(DOWN)

    tr, tc = query(instructions)

    if tc == s + 1 and W > 4:
        return CASE_LEFTMOST_COLUMN

    # only for even width cases
    if W % 2 == 0 and tc == s:
        return CASE_RIGHT_SIDE

    # only for odd width cases
    if W % 2 == 1 and (tr == H - 1 and tc == s):
        return CASE_RIGHT_SIDE

    return CASE_LEFT_SIDE


def find_box(case):
    instructions = []

    if case == CASE_LEFTMOST_COLUMN:
        instructions.append(DOWN * H)
        tr, tc = query(instructions)
        return (tr + 1, tc)

    # We KNOW the box is in a specific half, so we don't need to "bump into it"
    # if it's in the outermost column. As long as we make sure we never bump into
    # the opposite half's side wall, we can guarantee to arrive below the box in
    # the bottom row. Exception being if the box is in the bottom row.
    s = W // 2 - 1 if case == CASE_LEFT_SIDE or W % 2 == 0 else W // 2

    # instructions.extend(handle_first_row)

    # go to right corner
    if case == CASE_LEFT_SIDE:
        instructions.extend([RIGHT * W, DOWN, RIGHT * W, UP])
    instructions.append(LEFT * s)

    for _ in range(H):
        instructions.append(LEFT * s)
        instructions.append(RIGHT * s)
        instructions.append(DOWN)

    instructions.append(LEFT * s)
    instructions.append(LEFT)
    instructions.append(UP * H)

    # invert lefts and rights if not left
    if case == CASE_RIGHT_SIDE:
        instructions = mirror(instructions)

    tr, tc = query(instructions)

    if tr != 0:
        box_pos = (tr - 1, tc)
    else:
        box_pos = (H - 1, tc + 1 if case == CASE_RIGHT_SIDE else tc - 1)

    return box_pos


case = check_left_half()

print(["leftmost column", "right side", "left side"][case-1], file=stderr)

box_pos = find_box(case)

answer(*box_pos)
