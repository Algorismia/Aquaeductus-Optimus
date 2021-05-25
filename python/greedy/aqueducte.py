import sys
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


class Circumference:

    def __init__(self, point: Point, radius: int):
        self.point = point
        self.radius = radius

    @staticmethod
    def get_from_points(first: Point, second: Point, max_height: int) -> 'Circumference':
        radius = first.x_distance_to(second) / 2
        x_coord = (first.x_coord + second.x_coord) / 2
        y_coord = max_height - radius
        return Circumference(Point(x_coord, y_coord), radius)

    def point_is_outside(self, point: Point) -> bool:
        return (pow(self.point.distance(point), 2) - (pow(self.radius, 2))) > 0

    def point_is_higher(self, point: Point) -> bool:
        return self.point.y_coord < point.y_coord

    def some_point_is_higher(self, first_point: Point, second_point: Point) -> bool:
        return self.point_is_higher(first_point) or self.point_is_higher(second_point)


class Land:

    def __init__(self, num_points: str, max_height: str, alpha: str, beta: str):
        self.num_points = int(num_points)
        self.max_height = int(max_height)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.points = []
        self.point_values_buffer = [None] * self.num_points

    def add_point_to_land(self, x_coord: int, y_coord: int):
        self.points.append(Point(x_coord, y_coord))

    # cost related

    def cost_arch(self, first_point: Point, second_point: Point):
        return self.beta * pow(first_point.x_distance_to(second_point), 2)

    def cost_support(self, point: Point):
        return self.alpha * (self.max_height - point.y_coord)

    def total_cost(self, first_point_index: int, second_point_index: int):
        cost_first_point = self.cost_support(self.points[first_point_index])
        cost_arch = self.cost_arch(self.points[first_point_index], self.points[second_point_index])
        cost_second_point = self.point_values_buffer[second_point_index]
        if cost_second_point:
            return cost_first_point + cost_arch + cost_second_point
        return cost_first_point + cost_arch + self.cost_support(self.points[second_point_index])

    # validity of arch

    def some_point_outside_circumference(self, index_1: int, index_2: int, circle: Circumference):
        for i in range(index_1 + 1, index_2):
            if circle.point_is_higher(self.points[i]) and circle.point_is_outside(self.points[i]):
                return True
        return False

    def valid_arch(self, first_index: int, second_index: int) -> bool:
        first_point = self.points[first_index]
        second_point = self.points[second_index]
        semi_circ = Circumference.get_from_points(first_point, second_point, self.max_height)
        return not semi_circ.some_point_is_higher(first_point, second_point) and \
               not self.some_point_outside_circumference(first_index, second_index, semi_circ)

    # algorithm

    def get_minimum_aqueduct(self, current_point=0):
        if current_point == self.num_points - 1:
            return self.cost_support(self.points[current_point])
        minimum = math.inf
        minimum_point = None
        for i in range(current_point + 1, self.num_points, 1):
            if self.valid_arch(current_point, i):
                cost = self.total_cost(current_point, i)
                if cost < minimum:
                    minimum = cost
                    minimum_point = i
        if minimum == math.inf:
            return math.inf
        return minimum - self.cost_support(self.points[minimum_point]) +\
               self.get_minimum_aqueduct(minimum_point)


def get_land_from_file(my_file) -> Land:
    lines = my_file.readlines()
    num_points, max_height, alpha, beta = lines[0].split(" ")
    land = Land(num_points, max_height, alpha, beta)
    add_points_to_land(land, lines[1:])
    my_file.close()
    return land


def add_points_to_land(land: Land, points: list):
    for point in points:
        x_coord, y_coord = point.split("\n")[0].split(" ")
        land.add_point_to_land(int(x_coord), int(y_coord))


def get_file():
    if len(sys.argv) == 2:
        return open(sys.argv[1], "r")
    return sys.stdin


def main():
    sys.setrecursionlimit(100000)
    file_aqueduct = get_file()
    land = get_land_from_file(file_aqueduct)
    value = land.get_minimum_aqueduct()
    if value == math.inf:
        print("impossible")
    else:
        print(value)


if __name__ == "__main__":
    main()
