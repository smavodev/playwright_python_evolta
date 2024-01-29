import time
import warnings
import csv
from datetime import datetime
import pandas as pd

# Ignorar advertencias específicas
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas")

# Obtener la fecha actual para incluir en el nombre del archivo
current_date_str = datetime.now().strftime('%d-%m-%Y')

# Archivos para almacenar los datos con el nombre de archivo + fecha actual
csv_file_path = f'tiempos_de_carga_{current_date_str}.csv'
excel_file_path = f'tiempos_de_carga_{current_date_str}.xlsx'


def measure_load_time(page, action, selector, timeout):
    start_time = time.time()
    action()

    try:
        page.wait_for_selector(selector, timeout=timeout * 1000)
    except:
        print("Elemento no encontrado después de la acción.")

    end_time = time.time()
    load_time = round(end_time - start_time, 2)
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M:%S')
    current_date = current_datetime.strftime('%d-%m-%Y')

    print(f"Tiempo de carga después de {action.__name__}: {load_time} segundos")

    # Guardar los datos en el archivo CSV
    with open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Agregar cabecera si el archivo está vacío
        if csv_file.tell() == 0:
            csv_writer.writerow(['Fecha', 'Hora', 'Accion', 'Tiempo de Carga'])

        csv_writer.writerow([current_date, current_time, action.__name__, load_time])

    # Guardar los datos en el archivo Excel
    try:
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Fecha', 'Hora', 'Accion', 'Tiempo de Carga'])

    new_data = pd.DataFrame({'Fecha': [current_date], 'Hora': [current_time], 'Accion': [action.__name__], 'Tiempo de Carga': [load_time]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(excel_file_path, index=False)

