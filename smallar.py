NumList = []
Number = int(input("  "))
for i in range(1, Number + 1):
    value = int(input(" %d " %i))
    NumList.append(value)
print(min(NumList))
print(max(NumList))
