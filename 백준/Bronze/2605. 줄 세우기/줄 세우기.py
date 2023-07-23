import sys

N = int(sys.stdin.readline().rstrip())
lst = list()
lines = sys.stdin.readline().rstrip().split()
for idx, line in enumerate(lines):
    lst.insert(idx-int(line), str(idx+1))
print(" ".join(lst))