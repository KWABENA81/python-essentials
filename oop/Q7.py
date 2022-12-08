
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value: " + str(self.x) + \
            " y-value: " + str(self.y)

    def __add__(self, other):
        p = self
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p


def run_code():
    p1 = Point(3, 4)
    p2 = Point(2, 3)
    print(p1 + p2)


if __name__ == '__main__':
    run_code()
