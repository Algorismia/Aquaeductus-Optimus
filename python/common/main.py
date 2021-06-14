import math
import sys
from land import Land


def get_land_from_file(my_file, type_land) -> Land:
    lines = my_file.readlines()
    num_points, max_height, alpha, beta = lines[0].split(" ")
    land = type_land(num_points, max_height, alpha, beta)
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


def main(land_type):
    sys.setrecursionlimit(100000)
    file_aqueduct = get_file()
    land = get_land_from_file(file_aqueduct, land_type)
    value = land.algorithm()
    if value == math.inf:
        print("impossible")
    else:
        print(value)
