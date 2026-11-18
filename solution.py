import heapq

def solve(value):
    return list(heapq.merge(*value))
