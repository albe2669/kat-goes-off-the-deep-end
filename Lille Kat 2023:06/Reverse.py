n = int(input())
num = []
for i in range(n):
    num.append(input())

num.reverse()
for j in range(n):
    print(num[j])