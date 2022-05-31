from csv_util import read_csv_to_matrix
from algoritma import dijkstra, lintasan


def fetchAllNodes():
    graf = read_csv_to_matrix('assets/Matriks.csv')
    return graf

def shortestPath(start, end):
    graf = read_csv_to_matrix('assets/Matriks.csv')

    simpul_dipilih = dijkstra(graf,start)

    return {
        'start': start,
        'end': end,
        'path': lintasan(end, simpul_dipilih[end], simpul_dipilih),
        'distance': simpul_dipilih[end][0]
    }

def main():

    graf = read_csv_to_matrix('assets/Matriks.csv')

    awal = 0
    akhir = 12

    simpul_dipilih = dijkstra(graf,awal)

    print(f'start/end nodes: {awal} -> {akhir}')
    print('Tabel Hasil :')
    for tujuan, simpul in enumerate(simpul_dipilih):
        print(f"Simpul Tujuan : {tujuan}\tLintasan Terakhir : {simpul[1]}\tJarak : {simpul[0]}")

    print('shortest path:')
    print(lintasan(akhir, simpul_dipilih[akhir], simpul_dipilih))
    print(f'total distance: {simpul_dipilih[akhir][0]}')


if __name__ == '__main__':
    main()