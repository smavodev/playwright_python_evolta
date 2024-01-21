import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


# pytest --slowmo 2000  --headed input2.py

def test_checkbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context=browser.new_context()
    context = browser.new_context(record_video_dir="Videos/Checkbox")
    context = browser.new_context(
        viewport={'width': 1500, 'height': 1000}
    )

    page = context.new_page()
    # page.set_viewport_size({"width": 600, "height": 700})
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html")
    expect(page).to_have_title("Formulario de Ejemplo")

    # Tiempo de Espera
    page.set_default_timeout(3000)

    page.locator("//input[contains(@id,'campo1')]").fill("Rodrigo")
    page.locator("//input[@id='campo2']").fill("978546123")

    # Primero
    che1 = page.locator("//label[@for='opcion1']")
    expect(che1).to_be_visible()
    che1.click()

    # Segundo
    page.locator("//label[@for='opcion2']").click()

    # Selecciona una o más opciones:
    # Primero
    page.locator("//input[@value='opcionA']").click()

    # Segundo
    select2 = page.locator("//label[contains(@for,'opcionB')]")
    expect(select2).to_be_visible()
    select2.click()

    # Botón
    page.locator("//button[@type='submit']").click()

    confirm = page.locator("//div[contains(@id,'mensajeExito')]")
    expect(confirm).to_contain_text("Formulario enviado correctamente.")

    # Cerrar Context y Navegador
    context.close()
    browser.close()




