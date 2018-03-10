def reverseBits(n):
    result = 0
    i = 31
    while n:
        result += (n % 2) * 2 ** i
        i -= 1
        n = n // 2
    return result

print(reverseBits(43261596))
