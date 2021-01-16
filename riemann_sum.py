"""
    This program is created with the intent of solving the exercise problem from MAT136 Asynchronous
    Block video (3/4) from Week 1.
"""
import math


def compute_riemann_sums_in_sinx(domain: tuple, n: int) -> float:
    """
    This function computes the riemann sum given an <interval>
    and the number of rectangles, n

    It uses the right-endpoint technique to do so.

    >>> compute_riemann_sums_in_sinx((0, math.pi), 4)
    1.896
    """
    total_area, i = 0, 1                                        # i is the interval

    base = (domain[1] - domain[0]) / n                          # compute the base

    while i < n:
        height = math.sin(base * i)                             # compute the height
        total_area += base * height                             # area = l * w
        i += 1

    return round(total_area, 3)

x = compute_riemann_sums_in_sinx((0,math.pi), 200)
print(x) # prints 2.0 :)