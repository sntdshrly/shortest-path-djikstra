from csv_util import read_csv_to_matrix
from algoritma import dijkstra, dijkstra_2

def main():
    # graf = [
    #     [0,3,0,7,0,8,0],
    #     [3,0,4,2,0,0,0],
    #     [0,4,0,5,6,0,0],
    #     [7,2,5,0,8,3,0],
    #     [0,0,6,8,0,0,0],
    #     [8,0,0,3,0,0,1],
    #     [0,0,0,0,0,1,0],
    # ]

    graf = read_csv_to_matrix('assets/dijkstra.csv')

    # simpul a = 0

    awal = 0
    akhir = 11

    # simpul_dipilih = dijkstra(awal,tujuan,graf)
    simpul_dipilih = dijkstra_2(graf,awal)

    
    def lintasan(simpul, graf_hasil):
        if simpul[1] == None:
            return ' Selesai'
        print('<-', end='')
        print(simpul[1], end='')
        return lintasan(graf_hasil[simpul[1]], graf_hasil)

    print(f'start/end nodes: {awal} -> {akhir}')
    print('Tabel Hasil :')
    for tujuan, simpul in enumerate(simpul_dipilih):
        print(f"Simpul Tujuan : {tujuan}\tLintasan Terakhir : {simpul[1]}\tJarak : {simpul[0]}")

    print('shortest path:')
    print(akhir, end='')
    print(lintasan(simpul_dipilih[akhir], simpul_dipilih))
    print(f'total distance: {simpul_dipilih[akhir][0]}')


if __name__ == '__main__':
    main()