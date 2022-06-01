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
    pass


if __name__ == '__main__':
    main()