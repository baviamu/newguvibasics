import math
N=int(input(" "))
M=int(input(" "))
c=N*M
root = math.sqrt(c)
if int(root + 0.5) ** 2 == c:
    print("yes")
else:
    print("no")
