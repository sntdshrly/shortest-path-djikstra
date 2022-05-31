def dijkstra_2(awal : int, tujuan : int, graf : list) -> list:
    pointer = awal
    simpul_tersedia = []
    simpul_dipilih = [[awal,None,0]]

    while pointer != tujuan:

        simpul = graf[pointer]

        for i in range(0,len(simpul),1):

            if simpul[i] != 0 and i not in [j[0] for j in simpul_dipilih]:
                
                if i in [j[0] for j in simpul_tersedia]:
                    cek_minimal_jarak_simpul(simpul_tersedia, simpul, simpul_dipilih, i)
                else:
                    simpul_tersedia.append([i,pointer,simpul[i]+simpul_dipilih[-1][2]])
        
        simpul_minimal = simpul_tersedia[0]
        
        for vertex in simpul_tersedia:
            
            if vertex[2] < simpul_minimal[2]:
                simpul_minimal = vertex
       
        simpul_dipilih.append(simpul_minimal)
        next_pointer = simpul_tersedia.pop(simpul_tersedia.index(simpul_minimal))
        pointer = next_pointer[0]
    
    return simpul_dipilih


def cek_minimal_jarak_simpul(simpul_sekarang, kandidat, simpul_sebelumnya, index_simpul):
    index = [j[0] for j in simpul_sekarang].index(index_simpul)
    if kandidat[index_simpul]+simpul_sebelumnya[-1][2] < simpul_sekarang[index][2]:
            simpul_sekarang[index][1] = simpul_sebelumnya[-1][0]
            simpul_sekarang[index][2] = kandidat[index_simpul]+simpul_sebelumnya[-1][2]


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

def lintasan_2(simpul, graf_hasil):
    if simpul[1] == None:
        return ' Selesai'
    print('<-', end='')
    print(simpul[1], end='')
    return lintasan_2(graf_hasil[simpul[1]], graf_hasil)

def lintasan(akhir, simpul, graf_hasil):
    array_simpul = [akhir]
    while simpul[1] != None:
        array_simpul.append(simpul[1])
        simpul = graf_hasil[simpul[1]]
    return array_simpul