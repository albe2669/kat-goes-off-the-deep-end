from sys import stdin


"""
IDEA

steps:
- determine half:
    - go W/2 right
    - go down, W/2 left, W/2 right
    - repeat until hitting bottom. If you are located on the right half, you know it was in the left half. If not, then it must be in the right half
    - remember handling edge case of box being in the first row
- then determine both column and row in a single query:
    - use same strategy for column, but since we KNOW that the box is in that half, we will not end in the outermost column. therefore we can move one extra out in the final step and then try to go all the way up since the box must be in that column. we then must stop by hitting the box, revealing the row. if we reach the top, the row must have been the bottom row
"""


def next_line():
    return tuple(int(x) for x in next(stdin).split())


def query(instructions):
    print(f"? {''.join(instructions)}", flush=True)
    return next_line()


def answer(r, c):
    print(f"! {r} {c}", flush=True)


LEFT, RIGHT, UP, DOWN = "<>^v"

H, W = next_line()

# todo: handle odd
w = W // 2


# Handle edge case of box in being in the first row
handle_first_row = [DOWN, RIGHT * w, UP, LEFT * w, UP]


def check_left_half():
    instructions = []
    instructions.extend(handle_first_row)

    # Go to the right half and go down. Then all the way left again, go back out.
    # If the box is in the left half, we will hit the box when going left in some row.
    for _ in range(H):
        instructions.append(LEFT * w)
        instructions.append(RIGHT * w)
        instructions.append(DOWN)

    tr, tc = query(instructions)

    # If stop column is greater than w, then we hit the box going left in some row.
    # If we didn't get to the bottom, the box must be in the w column
    is_in_left = (tc > w) or (not tr < H - 1)

    return is_in_left

def find_box(is_in_left_half):
    instructions = []
    instructions.extend(handle_first_row)

    instructions.append(LEFT * w)
    instructions.append(RIGHT * w)

    # We KNOW the box is in a specific half, so we don't need to "bump into it"
    # if it's in the outermost column. As long as we make sure we never bump into
    # the opposite half's side wall, we can guarantee to arrive below the box in
    # the bottom row. Exception being if the box is in the bottom row.
    v = w - 1

    for _ in range(H):
        instructions.append(LEFT * v)
        instructions.append(RIGHT * v)
        instructions.append(DOWN)

    # also handle for the odd-width case...

    instructions.append(LEFT * v)
    instructions.append(LEFT)
    instructions.append(UP * H)

    # invert lefts and rights if not left
    if not is_in_left_half:
        go_to_right = [RIGHT * W, DOWN, RIGHT * W, UP]
        mirrored = [LEFT if x == RIGHT else RIGHT if x == LEFT else x for x in instructions]
        instructions = go_to_right + mirrored

    tr, tc = query(instructions)

    if tr != 0:
        box_pos = (tr - 1, tc)
    else:
        box_pos = (H - 1, tc - 1)

    return box_pos


is_in_left_half = check_left_half()
box_pos = find_box(is_in_left_half)

answer(*box_pos)
