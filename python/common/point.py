import math


class Point:

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def x_distance_to(self, second_point: 'Point') -> int:
        return second_point.x_coord - self.x_coord

    def y_distance_to(self, second_point: 'Point') -> int:
        return second_point.y_coord - self.y_coord

    def distance(self, second_point: 'Point') -> float:
        return math.sqrt(pow(self.x_distance_to(second_point), 2) + \
                         pow(self.y_distance_to(second_point), 2))
