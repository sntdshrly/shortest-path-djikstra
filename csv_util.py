import csv

def read_csv_to_matrix(file):
    array = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # asumsi baris 0 adalah header
            if line_count != 0:
                array.append([int(i) for i in row])
            line_count += 1
        print(f'Processed {line_count} lines.')
        # return matrix
        return array

def write_csv():
    pass