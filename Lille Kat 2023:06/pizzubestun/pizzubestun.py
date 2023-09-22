n = int(input())
prices = sorted(int(input().split()[1]) for _ in range(n))
print(sum(prices[-1::-2]))
