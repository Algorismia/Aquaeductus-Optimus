# pylint: disable=wrong-import-position
# pylint: disable=import-error
import sys
import math
sys.path.insert(1, '../common')
from land import Land
from main import main


class LandAlgorithm(Land):

    def algorithm(self):
        return self.get_minimum_aqueduct()

    def get_minimum_aqueduct(self, current_point=0) -> int:
        accumulator = self.cost_support(self.points[current_point])
        while current_point != self.num_points - 1:
            cost, current_point = self.get_minimum_arch(current_point)
            if cost == math.inf:
                return math.inf
            accumulator += cost
        return accumulator

    def get_minimum_arch(self, init_point: int) -> tuple:
        minimum, minimum_point = math.inf, None
        for i in range(init_point + 1, self.num_points, 1):
            if self.valid_arch(init_point, i):
                cost = self.total_cost(init_point, i)
                if cost < minimum:
                    minimum, minimum_point = cost, i
        return minimum - self.cost_support(self.points[init_point]), minimum_point


if __name__ == "__main__":
    main(LandAlgorithm)
