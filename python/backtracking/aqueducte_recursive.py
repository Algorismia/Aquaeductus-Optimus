# pylint: disable=wrong-import-position
# pylint: disable=import-error
import math
import sys
sys.path.insert(1, '../common')
from land import Land
from main import main


class LandAlgorithm(Land):

    def algorithm(self):
        return self.get_minimum_aqueduct()

    def get_minimum_aqueduct(self, current_point_index=0):
        # base case
        if current_point_index + 1 == self.num_points:
            return self.cost_support(self.points[current_point_index])
        # backtrack
        min_cost = math.inf
        for i in range(current_point_index + 1, self.num_points):
            if self.valid_arch(current_point_index, i):
                cost_previous = self.get_minimum_aqueduct(i)
                cost_previous += self.cost_support(self.points[current_point_index])
                cost_previous += self.cost_arch(self.points[current_point_index], self.points[i])
                min_cost = min(cost_previous, min_cost)
        return min_cost


if __name__ == "__main__":
    main(LandAlgorithm)
