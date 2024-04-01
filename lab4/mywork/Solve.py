def generator(g, prime,range_prime):
    w = set()
    for pows in range(1,prime):
        num = pow(g,pows,prime)
        w.add(num)
    return len(w) == prime - 1
