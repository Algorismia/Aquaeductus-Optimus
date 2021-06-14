import math
from enum import Enum
import sys
#pylint: disable=wrong-import-position
sys.path.insert(1, '../common')  # pylint: disable=import-error
from land import Land  # pylint: disable=import-error
from main import main  # pylint: disable=import-error


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
            current_context = my_stack.pop()
            if current_context.entry == EntryPoint.CALL:
                if current_context.index + 1 == self.num_points:
                    return_ = self.cost_support(self.points[current_context.index])
                else:
                    current_context.entry = EntryPoint.RESUME
                    my_stack.append(current_context)
                    if self.valid_arch(current_context.index, current_context.next_index):
                        current_context.actual_min = self.cost_arch(self.points[current_context.index],
                                                     self.points[current_context.next_index]) + \
                                                     self.cost_support(self.points[current_context.index])
                        my_stack.append(Context(current_context.next_index, EntryPoint.CALL))
                    else:
                        return_ = math.inf
            else:
                current_context.next_index += 1
                if current_context.actual_min + return_ < current_context.min_cost:
                    current_context.min_cost = current_context.actual_min + return_
                if current_context.next_index == self.num_points:
                    return_ = current_context.min_cost
                else:
                    current_context.entry = EntryPoint.CALL
                    my_stack.append(current_context)
        return return_


if __name__ == "__main__":
    main(LandAlgorithm)
