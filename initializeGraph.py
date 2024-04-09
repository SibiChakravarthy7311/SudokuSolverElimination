from collections import defaultdict


def initializeGraph():
    graph = defaultdict(set)
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                graph[(i, j)].add((i, k))
                graph[(i, k)].add((i, j))
            for k in range(i+1, 9):
                graph[(i, j)].add((k, j))
                graph[(k, j)].add((i, j))
            top = (i // 3) * 3
            left = (j // 3) * 3
            for k in range(top, top+3):
                if k == i:
                    continue
                for l in range(left, left+3):
                    if l == j:
                        continue
                    graph[(i, j)].add((k, l))
                    graph[(k, l)].add((i, j))
    return graph
