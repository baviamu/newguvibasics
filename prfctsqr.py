import math
N,M=(map(int,input().split()))
c=N*M
root = math.sqrt(c)
if int(root + 0.5) ** 2 == c:
    print("yes")
else:
    print("no")
