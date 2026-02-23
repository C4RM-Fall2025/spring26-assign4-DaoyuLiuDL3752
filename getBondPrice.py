def getBondPrice(y, face, couponRate, m, ppy=1):
    c = face * couponRate / ppy
    r = y / ppy
    n = int(m * ppy)
    return c * (1 - (1 + r) ** (-n)) / r + face * (1 + r) ** (-n) if r != 0 else c * n + face

