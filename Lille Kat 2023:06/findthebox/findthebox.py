from sys import stdin
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

    if tr == H - 1 and tc == s:
        return CASE_RIGHT_SIDE

    if tc == s + 1:
        return CASE_LEFTMOST_COLUMN

    return CASE_LEFT_SIDE


def find_box(case):
    instructions = []

    if case == CASE_LEFTMOST_COLUMN:
        instructions.append(DOWN * H)
        tr, tc = query(instructions)
        return (tr + 1, tc)

    instructions.extend(handle_first_row)

    # instructions.append(LEFT * w)
    # instructions.append(RIGHT * w)

    # We KNOW the box is in a specific half, so we don't need to "bump into it"
    # if it's in the outermost column. As long as we make sure we never bump into
    # the opposite half's side wall, we can guarantee to arrive below the box in
    # the bottom row. Exception being if the box is in the bottom row.
    s = W // 2 - 1 if case == CASE_LEFT_SIDE else W // 2

    if case == CASE_LEFT_SIDE:
        instructions.append(RIGHT * w)

    for _ in range(H):
        instructions.append(LEFT * s)
        instructions.append(RIGHT * s)
        instructions.append(DOWN)

    # also handle for the odd-width case...

    instructions.append(LEFT * s)
    instructions.append(LEFT)
    instructions.append(UP * H)

    # invert lefts and rights if not left
    if case == CASE_RIGHT_SIDE:
        go_to_right = [RIGHT * W, DOWN, RIGHT * W, UP]
        instructions = go_to_right + mirror(instructions)

    tr, tc = query(instructions)

    if tr != 0:
        box_pos = (tr - 1, tc)
    else:
        box_pos = (H - 1, tc + 1 if case == CASE_RIGHT_SIDE else tc - 1)

    return box_pos


is_in_left_half = check_left_half()
box_pos = find_box(is_in_left_half)

answer(*box_pos)