import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


# pytest --slowmo 2000  --headed input2.py

# def test_input2(page: Page):
def test_input2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context=browser.new_context()
    context = browser.new_context(record_video_dir="Videos/Input")
    context = browser.new_context(viewport={'width': 1500, 'height': 800})

    page = context.new_page()
    # page.set_viewport_size({"width": 600, "height": 700})
    page.goto("https://validaciones.rodrigovillanueva.com.mx/index.html")
    expect(page).to_have_title("Formulario de Ejemplo")

    # Tiempo de Espera
    page.set_default_timeout(5000)

    page.locator("//input[contains(@id,'nombre')]").fill("Rodrigo")
    page.screenshot(path="Imagenes/input2/nombre.png")

    # Aserts o Validadores
    apellidos = page.locator("//input[contains(@id,'apellidos')]")
    # Visible
    expect(apellidos).to_be_visible()
    page.locator("//input[contains(@id,'apellidos')]").fill("Villanueva Nieto")
    page.screenshot(path="Imagenes/input2/apellido.png")

    # Enabled
    email = page.locator("//input[contains(@id,'email')]")
    expect(email).to_be_enabled()
    # Empty tiene que estar Vacio
    expect(email).to_be_empty()

    page.locator("//input[contains(@id,'tel')]").fill("1978554490")
    page.screenshot(path="Imagenes/input2/telefono.png")

    # Contiene el ID
    expect(email).to_have_id("email")
    page.locator("//input[contains(@id,'email')]").fill("rodrigo@gmail.com")
    page.screenshot(path="Imagenes/input2/email.png")
    # tiempo forzado
    time.sleep(0.5)

    page.locator("//input[contains(@name,'direccion')]").fill("Testing #123 San Isidro")
    page.screenshot(path="Imagenes/input2/direccion.png")

    # Validar si esta Visible
    boton=page.locator("//button[@type='submit'][contains(.,'Enviar')]")
    expect(boton).to_be_visible()

    boton = page.is_visible("//button[@type='submit'][contains(.,'Enviar')]")  # True o False
    print(boton)
    if boton:
        print("Entro al True, es decir si lo encontro")
        page.locator("//button[@type='submit'][contains(.,'Enviar')]").click()
    else:
        print("No se Encuentar el Boton")
        print(boton)
    page.screenshot(path="Imagenes/input2/submit3.png")

    # expect(page).to_have_url(re.compile(".*datos-personales/"))

    CONFIRMACION = page.locator("//div[contains(@id,'flashMessage')]")
    expect(CONFIRMACION).to_contain_text("El formulario se ha enviado correctamente.")

    # Cerrar Context y Navegador
    context.close()
    browser.close()





