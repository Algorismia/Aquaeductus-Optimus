import sys
import math
#pylint: disable=wrong-import-position
sys.path.insert(1, '../common')  # pylint: disable=import-error
from land import Land  # pylint: disable=import-error
from main import main  # pylint: disable=import-error


class LandAlgorithm(Land):

    def algorithm(self):
        return self.get_minimum_aqueduct(0, self.cost_support(self.points[0]))

    def get_minimum_arch(self, init_point: int) -> tuple:
        minimum, minimum_point = math.inf, None
        for i in range(init_point + 1, self.num_points, 1):
            if self.valid_arch(init_point, i):
                cost = self.total_cost(init_point, i)
                if cost < minimum:
                    minimum, minimum_point = cost, i
        return minimum - self.cost_support(self.points[init_point]), minimum_point

    def get_minimum_aqueduct(self, current_point, accumulator) -> int:
        if current_point == self.num_points - 1:
            return accumulator
        cost, point_index = self.get_minimum_arch(current_point)
        if cost == math.inf:
            return math.inf
        return self.get_minimum_aqueduct(point_index, accumulator + cost)


if __name__ == "__main__":
    main(LandAlgorithm)
