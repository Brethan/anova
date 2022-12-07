def linear_interpolation(p1: tuple[float], p2: tuple[float], x: float) -> float:
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    y = ((x2 - x) * y1) + ((x - x1) * y2)

    return y / (x2 - x1)


y = linear_interpolation((60, 3.1504), (120, 3.0718), 72)

print(round(y, 3))
