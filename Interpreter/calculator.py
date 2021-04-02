import math

PI = 3.1415926535897932


def logBaseX(n, x):
    return math.log(n, x)


def naturalLog(n):
    return math.log(n)


def cosine(deg):
    return math.cos(deg * PI / 180)


def cosineInv(rad):
    return math.acos(rad) * 180 / PI
