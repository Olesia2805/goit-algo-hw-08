"""
There are several network cables of different lengths,
they must be combined two at a time into one cable using connectors,
in the order that will result in the lowest costs.
The cost of connecting two cables is equal to the sum of their lengths,
and the total cost is equal to the sum of connecting all cables.

The task is to find a joining order that minimizes the total costs.
"""

import heapq
import random

def min_cost_to_connect(cable):
    if cable == 0:
        return 0
    
    heapq.heapify(cable)
    total = 0
    
    while cable:
        num = heapq.heappop(cable)
        total += num

    return total

if __name__ == "__main__":
    cable_ = [15, 4, 6, 8, 12]
    print(f"Min cost for {cable_}: {min_cost_to_connect(cable_)}")

    random_cable = [random.randint(1, 50) for _ in range(10)]
    print(f"Min cost for {random_cable}: {min_cost_to_connect(random_cable)}")

    # Min cost for [15, 4, 6, 8, 12]: 45
    # Min cost for [38, 10, 29, 13, 8, 37, 3, 44, 1, 4]: 187