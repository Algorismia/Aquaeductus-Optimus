import sys
import math
#pylint: disable=wrong-import-position
sys.path.insert(1, '../common')  # pylint: disable=import-error
from land import Land  # pylint: disable=import-error
from main import main  # pylint: disable=import-error


class LandAlgorithm(Land):

    # override cost function for dynamic programming

    def total_cost(self, first_point_index: int, second_point_index: int, buffer_points: list):
        cost_first_point = self.cost_support(self.points[first_point_index])
        cost_arch = self.cost_arch(self.points[first_point_index], self.points[second_point_index])
        cost_second_point = self.cost_support(self.points[second_point_index])
        if buffer_points[second_point_index]:
            cost_second_point = buffer_points[second_point_index]
        return cost_first_point + cost_arch + cost_second_point

    def algorithm(self):
        point_values_buffer = [None] * self.num_points
        return self.get_minimum_aqueduct_recursive(self.num_points - 2, point_values_buffer)

    def get_minimum_cost_for_index(self, index: int, point_values_buffer: list) -> int:
        minimum = math.inf
        for i in range(index + 1, self.num_points):
            if self.valid_arch(index, i):
                cost_points = self.total_cost(index, i, point_values_buffer)
                minimum = min(minimum, cost_points)
        return minimum

    def get_minimum_aqueduct_recursive(self, index: int, point_values_buffer: list):
        if index == 0:
            minimum_of_this_point = self.get_minimum_cost_for_index(index, point_values_buffer)
            return minimum_of_this_point
        point_values_buffer[index] = self.get_minimum_cost_for_index(index, point_values_buffer)
        return self.get_minimum_aqueduct_recursive(index - 1, point_values_buffer)


if __name__ == "__main__":
    main(LandAlgorithm)
