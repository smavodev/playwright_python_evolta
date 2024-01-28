import pytest
from Config.Config import Config
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
URL_BASE = os.getenv("URL_BASE")
USER_VALID = os.getenv("USER_VALID")
PASS_VALID = os.getenv("PASS_VALID")
BROWSER = os.getenv("BROWSER")
HEADLESS = os.getenv("HEADLESS")
HEADLESS = True if HEADLESS.lower() == 'true' else False


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
    def test_login_success(self, base_test):
        base_test.login_success(USER_VALID, PASS_VALID)

