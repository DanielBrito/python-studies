def deep_reverse(L):
    result = []
    for i in L:
        result.append(i[::-1])
    L[:] = result[::-1]
    return L
