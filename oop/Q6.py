# This is a sample Python script.
import math
import re
from math import sqrt


def diff(a, b):
    return a - b


class Point:
    def __init__(self, x1, y1, x2, y2):
        self.xA = x1
        self.yA = y1
        self.xB = x2
        self.yB = y2

    def dist(self):
        xdiff = diff(self.xA, self.xB)
        ydiff = diff(self.yA, self.yB)

        sqr_xdiff = math.pow(xdiff, 2)
        sqr_ydiff = math.pow(ydiff, 2)
        sqr_sum = sqr_xdiff + sqr_ydiff
        return math.sqrt(sqr_sum)


def run_code():
    #   Distance between 2 points: --> linear algebra
    #       1. (3,14) and 2. (10,6)

    pts = Point(3, 14, 10, 6)
    print(pts.dist())


if __name__ == '__main__':
    run_code()

