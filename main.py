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


if __name__ == '__main__':

    coordinatesVector = [(0, 0),
                         (1, 3),
                         (3, 4),
                         (2, 6),
                         (6, 8)]

    velocityVector = [0, 3, 2, 5, 1]

    dist = calculate_distance(coordinatesVector)
    time = calculate_time(dist, velocityVector)
    cur_vec = define_current_vector(time, 2.5)
    print(dist)
    print(time)
    print(cur_vec[0], cur_vec[1])
