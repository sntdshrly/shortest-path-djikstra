INFINITY = float('inf')

def dijkstra(graf, awal):
    L = [None] * len(graf)
    for i in range(len(graf)):
        L[i] = [INFINITY, None]
    
    L[awal] = [0, None]
    S = []

    for k in range(len(graf)):
        mini = INFINITY
        for j in range(len(graf)):
            if L[j][0] < mini and j not in S:
                mini = L[j][0]
                minind = j
        # [minind, , mini]
        S.append(minind)

        for i in [l for l in range(len(graf)) if l not in S]:
            if graf[minind][i] != 0:
                if L[i][0] > L[minind][0] + graf[minind][i]:
                    L[i][0] = L[minind][0] + graf[minind][i]
                    L[i][1] = minind
                    # L[i] = L[minind] + graf[minind][i]

    return L

def lintasan(akhir, simpul, graf_hasil):
    array_simpul = [akhir]
    while simpul[1] != None:
        array_simpul.append(simpul[1])
        simpul = graf_hasil[simpul[1]]
    return array_simpul