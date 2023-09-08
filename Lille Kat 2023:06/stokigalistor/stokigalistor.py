import sys

sys.stdin.readline()
nums = [int(x) for x in sys.stdin.readline().split()]
s = sorted(nums)
print(sum([nums[i] != s[i] for i in range(len(nums))]))
