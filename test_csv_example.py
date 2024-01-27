import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from Utils.Data_context import get_Data_from_CSV_2


@pytest.mark.parametrize("test_data", get_Data_from_CSV_2('Data\\data_users.csv'))
def test_input2(playwright: Playwright, test_data) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # page.set_viewport_size({"width": 1200, "height": 900})

    page.goto("https://test.evolta.pe/Login/Acceso/Index")
    expect(page).to_have_title("Evolta - CRM Inmobiliario")
    page.set_default_timeout(60000)

    # Llenar el formulario con los datos del CSV
    page.locator('//*[@id="txtUsuario"]').fill(test_data['username'])
    page.locator('//*[@id="txtClave"]').fill(test_data['password'])
    page.locator("//input[contains(@class,'btn btn-lg btn-danger btn-block')]").click()
    page.set_default_timeout(60000)

    page.locator("//a[@href='#'][contains(.,'Inicio')]").click()
    page.locator("//input[contains(@type,'search')]").fill(test_data['busqueda_a'])
    page.locator("//button[contains(.,'Buscar')]").click()
    # page.set_default_timeout(60000) # Implicit
    page.wait_for_timeout(6000)  # Explicit

    page.locator("//div[contains(@class,'dropdown drp-user')]").click()
    page.locator("//a[contains(.,'Salir')]").click()

    # Cerrar Context y Navegador
    context.close()
    browser.close()


