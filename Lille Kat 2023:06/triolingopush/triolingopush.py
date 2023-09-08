import sys

n = int(sys.stdin.readline())

mem = [1] * (n+2)
mem[0] = 1
mem[1] = 2

for i in range(2, n):
    mem[i] = mem[i-1] + mem[i-2]+1

print(mem[n-1])
