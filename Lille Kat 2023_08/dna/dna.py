from sys import stdin

N = int(next(stdin))
s = next(stdin)

flipped = False
num_bs = 0
mutations = 0

for i in range(N, -1, -1):
    c = s[i] if not flipped else ('A' if s[i] == 'B' else 'B')

    if c == 'A' and num_bs > 0:
        mutations += 1

        if num_bs > 1:
            flipped = not flipped
            c = 'B'

        num_bs = 0

    if c == 'B':
        num_bs += 1

if num_bs > 0:
    mutations += 1

print(mutations)
