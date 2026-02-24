def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    pv_sum = 0.0
    pv_t_sum = 0.0

    for t in range(1, n + 1):
        cf = c if t < n else c + face
        pv = cf / ((1 + r) ** t)
        pv_sum += pv
        pv_t_sum += t * pv

    return (pv_t_sum / pv_sum) / ppy

#commit again to make sure it's correct

