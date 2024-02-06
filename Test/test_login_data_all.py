import time

import pytest
from Config.Config import Config
from Utils.Data_context import get_Data_from_Excel, get_Data_from_CSV, get_Data_from_TXT
from Pages.LoginPage3 import LoginPage
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
URL_BASE = os.getenv("URL_BASE")
BROWSER = os.getenv("BROWSER")
HEADLESS = os.getenv("HEADLESS")
HEADLESS = True if HEADLESS.lower() == 'true' else False
RUTA_DATA = os.getenv("RUTA_DATA")
MES_INICI0 = os.getenv("MES_INICI0")
BUSQUEDA_A = os.getenv("BUSQUEDA_A")
VALIDACION_A = os.getenv("VALIDACION_A")
tiempo_espera = 30


@pytest.fixture(scope="module")
def browser():
    config = Config(browser=BROWSER, headless=HEADLESS)
    context = config.get_browser_context()
    yield context
    context.close()


@pytest.fixture
def base_test(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to_url(URL_BASE)
    yield login_page
    page.close()


class TestLoginSuccess:

    @pytest.mark.data_test
    @pytest.mark.parametrize("user_data", get_Data_from_TXT(RUTA_DATA + 'data_users.txt'))
    def test_login_success_0(self, base_test, user_data):
        start_time = time.time()

        username = user_data.get("username")
        password = user_data.get("password")

        base_test.login_success_(username, password, mes_inicio=MES_INICI0, tiempo=tiempo_espera)
        base_test.panelSeguimiento_(tiempo_espera)
        base_test.busquedaLeads_(BUSQUEDA_A, VALIDACION_A, tiempo_espera, )

        end_time = time.time()
        total_time = end_time - start_time
        rounded_total_time = round(total_time, 2)
        print(f"Tiempo total de ejecución: {rounded_total_time} segundos")

