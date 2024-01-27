import csv


def get_Data_from_CSV_1(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Omitir la primera fila si contiene encabezados
        for row in reader:
            data.append(tuple(row))
    return data


def get_Data_from_CSV_2(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

