def dijkstra(awal : int, tujuan : int, graf : list) -> list:
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

