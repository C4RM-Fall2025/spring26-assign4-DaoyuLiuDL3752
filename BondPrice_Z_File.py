def getBondPrice_Z(face, couponRate, times, yc):
    c = face * couponRate
    price = 0.0
    n = len(times)
    for i, (t, r) in enumerate(zip(times, yc), start=1):
        cf = c if i < n else c + face
        price += cf / ((1 + r) ** t)
    return price
# I can't believe it
