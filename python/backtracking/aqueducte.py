# pylint: disable=wrong-import-position
# pylint: disable=import-error
# pylint: disable=too-few-public-methods
import math
from enum import Enum
import sys
sys.path.insert(1, '../common')
from land import Land
from main import main


class EntryPoint(Enum):
    CALL = "CALL"
    RESUME = "RESUME"


class Context:

    def __init__(self, index: int, entry: EntryPoint):
        self.index = index
        self.entry = entry
        self.next_index = index + 1
        self.actual_min = math.inf
        self.min_cost = math.inf


class LandAlgorithm(Land):

    def algorithm(self):
        return self.get_minimum_aqueduct()

    def get_minimum_aqueduct(self, current_point_index=0):
        return_ = math.inf
        my_stack = [Context(current_point_index, EntryPoint.CALL)]
        while my_stack:
            current = my_stack.pop()
            if current.entry == EntryPoint.CALL:
                if current.index + 1 == self.num_points:
                    return_ = self.cost_support(self.points[current.index])
                else:
                    current.entry = EntryPoint.RESUME
                    my_stack.append(current)
                    if self.valid_arch(current.index, current.next_index):
                        current.actual_min = self.cost_arch(self.points[current.index],
                                                     self.points[current.next_index]) + \
                                                     self.cost_support(self.points[current.index])
                        my_stack.append(Context(current.next_index, EntryPoint.CALL))
                    else:
                        return_ = math.inf
            else:
                current.next_index += 1
                current.min_cost = min(current.actual_min + return_, current.min_cost)
                if current.next_index == self.num_points:
                    return_ = current.min_cost
                else:
                    current.entry = EntryPoint.CALL
                    my_stack.append(current)
        return return_


if __name__ == "__main__":
    main(LandAlgorithm)
