def zeros(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y
