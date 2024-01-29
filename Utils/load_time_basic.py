import time


def measure_load_time(page, action, selector, timeout):
    start_time = time.time()
    action()

    try:
        page.wait_for_selector(selector, timeout=timeout * 1000)
    except:
        print("Elemento no encontrado después de la acción.")

    end_time = time.time()
    load_time = end_time - start_time
    print(f"Tiempo de carga después de {action.__name__}: {load_time:.2f} segundos")

