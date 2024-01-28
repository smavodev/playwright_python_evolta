import pytest
from Config.Config import Config
from Pages.LoginPage import LoginPage

URL_BASE = "https://test.evolta.pe/Login/Acceso/Index"
USER_VALID = "yhernandez"
PASS_VALID = "Performance23!"
BROWSER = "chrome"


@pytest.fixture(scope="module")
def browser():
    config = Config(browser=BROWSER, headless=False)
    context = config.get_browser_context()
    yield context
    context.close()


@pytest.fixture
def login_page(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to_url(URL_BASE)
    yield login_page
    page.close()


class TestLoginSuccess:
    def test_login_success(self, login_page):
        login_page.login_success(USER_VALID, PASS_VALID)

