import time
import sys
import pytest
import schedule


# Definir la tarea de ejecutar pruebas
def run_tests():
    print("Ejecutando pruebas...")
    sys.stdout.flush()  # Asegurar que la salida se imprima inmediatamente
    pytest.main(["-v", "./Test/test_load_time_3.py"])


# Programar la ejecución de las pruebas cada 10 minutos durante 6 horas
schedule.every(1).minutes.do(run_tests)

# Mantener el programa en ejecución hasta que se completen las 6 horas
total_time = 1 * 60 * 60  # 8 horas en segundos
start_time = time.time()

while time.time() - start_time < total_time:
    schedule.run_pending()
    time.sleep(5)

