def numSetBits(A):
    num_bits = 0
    while A > 0:
        print A
        num_bits += int(bin(A)[len(bin(A)) - 1]) and 1
        A >>= 1
    return num_bits


print numSetBits(2)
