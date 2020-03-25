import heapq

def Greedy(map, start, goal):
    visited = set()
    parent = {}
    gn {start : 0}

    pq = []

    heapq.heappush(pq, (gn[start], start))