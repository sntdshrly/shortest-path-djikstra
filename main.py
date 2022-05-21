def main():
    graf = [
        [0,3,0,7,0],
        [3,0,4,2,0],
        [0,4,0,5,6],
        [7,2,5,0,4],
        [0,0,6,4,0],
    ]

    # simpul a = 0

    awal = 0
    tujuan = 4

    pointer = awal
    simpul_tersedia = []
    simpul_dipilih = [[awal,None,0]]

    while pointer != tujuan:
        simpul = graf[pointer]
        for i in range(0,len(simpul),1):
            if simpul[i] != 0 and i not in [j[0] for j in simpul_dipilih]:
                if i in [j[0] for j in simpul_tersedia]:
                    index = [j[0] for j in simpul_tersedia].index(i)
                    if simpul[i]+simpul_dipilih[-1][2] < simpul_tersedia[index][2]:
                        simpul_tersedia[index][1] = simpul_dipilih[-1][0]
                        simpul_tersedia[index][2] = simpul[i]+simpul_dipilih[-1][2]
                else:
                    simpul_tersedia.append([i,pointer,simpul[i]+simpul_dipilih[-1][2]])
        simpul_minimal = simpul_tersedia[0]
        for vertex in simpul_tersedia:
            if vertex[2] < simpul_minimal[2]:
                simpul_minimal = vertex
        simpul_dipilih.append(simpul_minimal)
        next_pointer = simpul_tersedia.pop(simpul_tersedia.index(simpul_minimal))
        pointer = next_pointer[0]

    print(simpul_dipilih)
    

if __name__ == '__main__':
    main()