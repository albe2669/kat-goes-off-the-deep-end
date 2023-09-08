# Solved in collaboration with Emil Dichmann
# Achieves 52/100 points due to TLE on scoring groups 5-7

n, _, k = map(int, input().split())
customers = [int(input()) for _ in range(n)]

machines = set()
cleanings = 0

for i, flavor in enumerate(customers):
    # Flavor already loaded
    if flavor in machines:
        continue
    # Load flavor into empty machine
    if len(machines) < k:
        machines.add(flavor)
        cleanings += 1
        continue

    # Find the machine that will be used last
    repeats = set()
    for j in range(i + 1, n):
        next_flavor = customers[j]
        if next_flavor in machines:
            repeats.add(next_flavor)
            if len(repeats) == k:
                machines.remove(next_flavor)
                break

    # Load flavor into newly cleaned machine
    machines.add(flavor)
    cleanings += 1

print(cleanings)
