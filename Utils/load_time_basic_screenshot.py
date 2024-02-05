import os
import time
from datetime import datetime


def measure_load_time(page, action, selector, t_espera, fNumber=1, folder=True):
    start_time = time.time()
    action()

    try:
        page.wait_for_selector(selector, timeout=t_espera * 1000)
    except:
        print("Elemento no encontrado después de la acción.")

    end_time = time.time()
    load_time = end_time - start_time

    screenshot_dir = os.path.abspath("screenshots")  # Directorio base para capturas de pantalla

    # Verificar y crear directorios si no existen
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Generar nombre de la carpeta basado en la función de acción y el número de carpeta
    action_name = action.__name__

    if folder:
        action_screenshot_dir = os.path.join(screenshot_dir, f"{fNumber}_{action_name}")
    else:
        action_screenshot_dir = screenshot_dir

    # Crear directorio de capturas de pantalla específico para esta acción si no existe
    if not os.path.exists(action_screenshot_dir):
        os.makedirs(action_screenshot_dir)

    # Obtener la fecha y hora actual en el formato deseado
    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    # Capturar captura de pantalla
    page.screenshot(path=os.path.join(action_screenshot_dir, f"{fNumber}_{action_name}_{current_time}.png"))

    print(f"Tiempo de carga después de {action.__name__}: {load_time:.2f} segundos")
