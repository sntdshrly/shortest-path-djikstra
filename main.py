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
    tujuan = 6

    # simpul_dipilih = dijkstra(awal,tujuan,graf)
    simpul_dipilih = dijkstra_2(graf,awal)

    for tujuan, simpul in enumerate(simpul_dipilih):
        print(f"Simpul Tujuan : {tujuan}\tLintasan Terakhir : {simpul[0]}\tJarak : {simpul[1]}")

    # print(f'start/end nodes: {awal} -> {tujuan}')
    # simpul_dipilih = list(simpul_dipilih)
    # print(f'shortest path: {[lst[0] for lst in simpul_dipilih]}')
    # print(f'total distance: {sum([lst[2] for lst in simpul_dipilih])}')


if __name__ == '__main__':
    main()