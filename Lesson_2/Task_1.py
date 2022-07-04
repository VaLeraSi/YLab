import math
import random

start_point = (0, 2)
points = [(2, 5), (5, 2), (6, 6), (8, 3)]
count_possible_route = math.factorial(len(points))
total = 0
random_distances = []
random_total = []
set_points = set()
for item in range(count_possible_route):
    point_1 = tuple(start_point)
    point_2 = random.choice(points)
    word = f'{point_1} ->'
    i = 0
    while i != len(points) + 1:
        if i == len(points):
            point_2 = tuple(start_point)
            distance = ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5
            total += distance
            word += f' {point_2}[{total}] '
            break
        elif point_2 not in set_points:
            distance = ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5
            total += distance
            word += f' {point_2}[{total}] ->'
            point_1 = point_2
            set_points.add(point_2)
            i += 1
        else:
            point_2 = random.choice(points)
    random_total.append(total)
    random_distances.append(word + f'= {total}')
    total = 0
    set_points = set()
for i in range(len(random_total)):
    if random_total[i] == min(random_total):
        print(random_distances[i])
        break
