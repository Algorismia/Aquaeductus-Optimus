from point import Point


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
