from typing import List
import heapq

def most_calories(caloric_loads: List[List[int]]) -> int:
    most_calories = 0
    for caloric_load in caloric_loads:
        caloric_load_sum = sum(caloric_load)
        most_calories = max(most_calories, caloric_load_sum)
    return most_calories

def top_three_calories(caloric_loads: List[List[int]]) -> int:
    heap = []
    for caloric_load in caloric_loads:
        caloric_load_sum = sum(caloric_load)
        if len(heap) < 3:
            heap.append(caloric_load_sum)
        else:
            heapq.heappushpop(heap, caloric_load_sum)
    return sum(heap)

if __name__ == '__main__':
    with open('./input1.txt', 'r') as f:
        data = f.read()
        caloric_loads = [list(map(int, load.split('\n'))) for load in data.split('\n\n')]
        print(most_calories(caloric_loads))
        print(top_three_calories(caloric_loads))