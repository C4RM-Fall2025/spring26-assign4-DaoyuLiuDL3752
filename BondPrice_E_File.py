def getBondPrice_E(face, couponRate, yc):
    c = face * couponRate
    price = 0.0
    m = len(yc)
    for t, r in enumerate(yc, start=1):
        cf = c if t < m else c + face
        price += cf / ((1 + r) ** t)
    return price
