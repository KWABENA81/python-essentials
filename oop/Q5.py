# This is a sample Python script.
import re


class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        #   correct way is to reference the class variable
        return self.width * self.height


def run_code():
    # box instance
    x = Box(10, 2)
    # Print area:
    print(x.area())


if __name__ == '__main__':
    run_code()
