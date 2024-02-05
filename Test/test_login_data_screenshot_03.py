import time

import pytest
from Config.Config import Config
from Utils.Data_context import get_Data_from_Excel, get_Data_from_CSV, get_Data_from_TXT
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
URL_BASE = os.getenv("URL_BASE")
# USER_VALID = os.getenv("USER_VALID")
# PASS_VALID = os.getenv("PASS_VALID")
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
    @pytest.mark.skip
    @pytest.mark.parametrize("user_data", get_Data_from_Excel(RUTA_DATA+'data_users.xlsx'))
    def test_login_success_0(self, base_test, user_data):
        base_test.login_success_1(user_data)

    @pytest.mark.skip
    @pytest.mark.parametrize("user_data", get_Data_from_Excel(RUTA_DATA+'data_users.xlsx'))
    def test_login_success_1(self, base_test, user_data):
        username = user_data.get("username")
        password = user_data.get("password")
        base_test.login_success_2(username, password, MES_INICI0, tiempo_espera)

    @pytest.mark.skip
    @pytest.mark.parametrize("user_data", get_Data_from_CSV(RUTA_DATA+'data_users.csv'))
    def test_login_success_2(self, base_test, user_data):
        username = user_data.get("username")
        password = user_data.get("password")
        base_test.login_success_2(username, password, MES_INICI0, tiempo_espera)

    @pytest.mark.skip
    @pytest.mark.parametrize("user_data", get_Data_from_TXT(RUTA_DATA+'data_users.csv'))
    def test_login_success_3(self, base_test, user_data):
        username = user_data.get("username")
        password = user_data.get("password")
        base_test.login_success_2(username, password, MES_INICI0, tiempo_espera)

    @pytest.mark.data_test
    @pytest.mark.parametrize("user_data", get_Data_from_TXT(RUTA_DATA + 'data_users.txt'))
    def test_login_success_4(self, base_test, user_data):
        start_time = time.time()  # Capturar el tiempo de inicio

        username = user_data.get("username")
        password = user_data.get("password")
        # seguimiento_a = user_data.get('busqueda_a')
        base_test.login_success_2(username, password, MES_INICI0, tiempo_espera)
        base_test.panelSeguimiento(tiempo_espera)
        base_test.busquedaLeads(BUSQUEDA_A, VALIDACION_A, tiempo_espera, )

        end_time = time.time()
        total_time = end_time - start_time
        rounded_total_time = round(total_time, 2)  # Redondear a 2 decimales
        print(f"Tiempo total de ejecución: {rounded_total_time} segundos")

