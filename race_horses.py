"""The 25 Horses Problem
There are 25 mechanical horses and a single racetrack.
Each horse completes the track in a pre-programmed time,
and the horses all have different finishing times, unknown to you.
You can race 5 horses at a time.
After a race is over, you get a printout with the order the horses finished,
but not the finishing times of the horses.
What is the minimum number of races you need to identify the fastest 3 horses?
"""
import random
from typing import NamedTuple


class Horse(NamedTuple):
    '''This class has initializes the speed and initial group and fn returns greater speed '''
    speed: int
    initial_group: int

    def __lt__(self, other):
        return self.speed < other.speed


pop = [random.randint(1, 100) for _ in range(25)]
print(*pop)

initial_groups = [[Horse(x, i) for x in pop[i * 5 : i * 5 + 5]] for i in range(5)]

# 5 runs
for group in initial_groups:
    group.sort(reverse=True)

# group with fastest of each initial
fastest_of_each = [group[0] for group in initial_groups]

# +1 run
fastest_of_each.sort(reverse=True)

# last group with:
#   - 2nd and 3rd place of group of overall fastest
#   - 2nd overall fastest and 2nd place of its group
#   - 3rd overall fastest
last_group = [
    initial_groups[fastest_of_each[0].initial_group][1],
    initial_groups[fastest_of_each[0].initial_group][2],
    fastest_of_each[1],
    initial_groups[fastest_of_each[1].initial_group][1],
    fastest_of_each[2],
]

# +1 run
last_group.sort(reverse=True)

print(fastest_of_each[0].speed, last_group[0].speed, last_group[1].speed)