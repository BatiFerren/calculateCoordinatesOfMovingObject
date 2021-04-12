import math


def calculate_distance(coordinatesVector):
    index = 0
    distance = []
    while index < (len(coordinatesVector) - 1):
        radius_n = math.sqrt(pow(abs(coordinatesVector[index + 1][0] - coordinatesVector[index][0]), 2) + pow(abs(coordinatesVector[index + 1][1] - coordinatesVector[index][1]), 2))
        distance.append(radius_n)
        index += 1
    return distance


def calculate_time(radiusVector, velocityVector):
    timeVector = []
    index = 0
    while index < len(radiusVector):
        time_n = radiusVector[index] / velocityVector[index + 1]
        index += 1
        timeVector.append(time_n)
    return timeVector


def define_current_vector(timesVector, t):
    n = 0
    current_time = 0
    for item in timesVector:
        current_time += item
        if current_time >= t: break
        n += 1
    return (current_time, n)


def distance_on_current_section(pair, t, timeVector, velocityVector):
    difference_of_time = pair[0] - t
    passed_time_on_current_section = timeVector[pair[1]] - difference_of_time
    passed_distance_on_current_section = velocityVector[pair[1] + 1] * passed_time_on_current_section
    return passed_distance_on_current_section


def get_current_coordinates(pair, coordinatesVector, passed_distance_on_current_section, distanses):
    coordinate_x = ((coordinatesVector[pair[1] + 1][0] - coordinatesVector[pair[1]][0]) * passed_distance_on_current_section)/distanses[pair[1]]
    result_x = coordinatesVector[pair[1]][0] + coordinate_x
    coordinate_y = ((coordinatesVector[pair[1] + 1][1] - coordinatesVector[pair[1]][1]) * passed_distance_on_current_section) / distanses[pair[1]]
    result_y = coordinatesVector[pair[1]][1] + coordinate_y
    result_coordinates = (result_x, result_y)
    return result_coordinates


if __name__ == '__main__':

    coordinatesVector = [(0, 0),
                         (1, 3),
                         (3, 4),
                         (2, 6),
                         (6, 8)]

    velocityVector = [0, 3, 2, 5, 1]

    t = 2.5

    dist = calculate_distance(coordinatesVector)
    time = calculate_time(dist, velocityVector)
    cur_vec = define_current_vector(time, t)
    cur_dist = distance_on_current_section(cur_vec, t, time, velocityVector)
    finish_coordinates = get_current_coordinates(cur_vec, coordinatesVector, cur_dist, dist)
    print(finish_coordinates)

