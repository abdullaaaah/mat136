"""
    This program is created with the intent of solving the exercise problem from MAT136 Asynchronous
    Block video (3/4) from Week 1.
"""
import math


def compute_riemann_sums_in_sinx(interval: tuple, n: int) -> float:
    """
    This function computes the riemann sum given an <interval>
    and the number of rectangles, n

    It uses the right-endpoint technique to do so.

    >>> compute_riemann_sums_in_sinx((0, math.pi), 4)
    1.896
    """
    sum, count = 0, 1

    width = (interval[1] - interval[0]) / n                # compute the width

    while count < n:
        right_endpoint = math.sin(width * count)           # compute the length
        sum += width * right_endpoint                      # area = l * w
        count += 1

    return round(sum, 3)

x = compute_riemann_sums_in_sinx((0,math.pi), 200)
print(x) # prints 2.0 :)