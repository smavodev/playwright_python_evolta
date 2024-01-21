from playwright.sync_api import Playwright, expect
from Funciones import Funciones_Globales

# Variables globales
tiempo = 0.5
ruta = "Imagenes/Select/"


def test_select1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context = browser.new_context(viewport={'width': 1500, 'height': 800})  # record_video_dir="Videos/Checkbox/" )
    page = context.new_page()
    page.goto("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html")

    page.set_default_timeout(8000)
    expect(page).to_have_title("Formulario de Ejemplo")

    # Creando nuestro Objeto de tipo Funciones Globales
    F = Funciones_Globales(page)
    F.Validar_titulo_pagina("Formulario de Ejemplo", 1.0)
    F.Esperar(tiempo)

    page.get_by_label("ComboBox 1:").select_option("4")
    page.screenshot(path=ruta+"Select_1.png")

    page.get_by_label("ComboBox 2 (Multi-selección):").select_option("1")
    page.screenshot(path=ruta+"Select_2.png")

    page.get_by_label("Sistema Operativo:").select_option("linux")
    page.screenshot(path=ruta + "SO.png")

    page.get_by_label("Versión:").select_option("Fedora")
    page.screenshot(path=ruta + "version.png")

    F.Click_img("//button[@type='button'][contains(.,'Enviar')]", ruta+"Boton.png", 1.0)

    F.Esperar(2)
    context.close()
    browser.close()
