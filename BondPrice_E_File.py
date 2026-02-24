def getBondPrice_E(face, couponRate, m, yc):
    c = face * couponRate
    price = 0.0
    for t, r in enumerate(yc[:m], start=1):
        cf = c if t < m else c + face
        price += cf / ((1 + r) ** t)
    return price
