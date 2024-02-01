import pytest
from playwright.sync_api import Playwright, sync_playwright
from Utils.Data_context import get_Data_from_TXT
import os
from dotenv import load_dotenv

load_dotenv()

RUTA_DATA = os.getenv("RUTA_DATA")


# Lanzar el navegador y crear el contexto fuera del bucle
@pytest.fixture
def browser_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()


# Parametrizar la prueba con los datos del CSV
@pytest.mark.parametrize("test_data", get_Data_from_TXT(RUTA_DATA+'data_users.csv'))
def test_input2(browser_context, test_data) -> None:
    context = browser_context
    page = context.new_page()

    page.goto("https://test.evolta.pe/Login/Acceso/Index")
    assert page.title() == "Evolta - CRM Inmobiliario"

    # Resto del código de la prueba
    page.locator('//*[@id="txtUsuario"]').fill(test_data['username'])
    page.locator('//*[@id="txtClave"]').fill(test_data['password'])
    page.locator("//input[contains(@class,'btn btn-lg btn-danger btn-block')]").click()
    page.set_default_timeout(60000)

    page.locator("//a[contains(.,'Inicio')]").click()
    page.locator("//input[contains(@type,'search')]").fill(test_data['busqueda_a'])
    page.locator("//button[contains(.,'Buscar')]").click()
    # page.wait_for_timeout(6000)
    page.set_default_timeout(6000)

    page.locator("//div[contains(@class,'dropdown drp-user')]").click()
    page.locator("//a[contains(.,'Salir')]").click()

    # # Cerrar la página al final de cada iteración
    page.close()
