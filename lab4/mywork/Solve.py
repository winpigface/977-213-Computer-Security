def gcb(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcb(b, a % b)


def set_H(g, prime):
    for i in range(1, prime):
        if (g**i) % prime == 1:
            print(i)
            return False
    return True
