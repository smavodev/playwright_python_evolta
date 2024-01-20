import re
from playwright.sync_api import Page, expect


def test_uno(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("apps"))

    buton_uno = page.locator("text=Get started")
    expect(buton_uno).to_have_attribute("href", "/docs/intro")
    page.screenshot(path="Imagenes/test_uno.png")
    buton_uno.click()
    # Tomar foto
    page.screenshot(path="Imagenes/test_uno_final.png")

    # Validando el resultado de la página destino
    expect(page).to_have_url(re.compile(".*docs/intro"))




