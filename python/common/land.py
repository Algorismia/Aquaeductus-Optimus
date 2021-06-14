from point import Point
from circumference import Circumference
from abc import ABC, abstractmethod


class Land(ABC):

    def __init__(self, num_points: str, max_height: str, alpha: str, beta: str):
        self.num_points = int(num_points)
        self.max_height = int(max_height)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.points = []

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
        cost_second_point = self.cost_support(self.points[second_point_index])
        return cost_first_point + cost_arch + cost_second_point

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

    @abstractmethod
    def algorithm():
        pass
