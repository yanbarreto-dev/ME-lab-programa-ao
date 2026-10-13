def comparar(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(comparar(4, 8))
print(comparar(3, 8))