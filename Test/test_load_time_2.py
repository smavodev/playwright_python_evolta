import re
import pytest
from playwright.sync_api import sync_playwright, expect
from Utils.load_time_basic import measure_load_time
from Config.Config import Config

URL_BASE = "https://demoqa.com/"
BROWSER = "chrome"


class TestSuccess:

    @pytest.fixture(scope="module")
    def browser(self):
        config = Config(browser=BROWSER, headless=False)
        context = config.get_browser_context()
        yield context
        context.close()

    @pytest.fixture
    def login_page(self, browser):
        page = browser.new_page()
        page.goto(URL_BASE)  # Utiliza el método goto para navegar a la URL base
        yield page
        page.close()

    def test_dos(self, login_page):

        def registro_test():
            # Hacer clic en "Elements"
            login_page.locator("text=Elements").click()
            expect(login_page).to_have_url(re.compile(".*elements"))

            # Hacer clic en "Text Box"
            login_page.locator("text=Text Box").click()
            expect(login_page).to_have_url(re.compile(".*text-box"))

        measure_load_time(login_page, registro_test, "text=Text Box", 30)

        def test_form():
            # Rellenar formularios
            login_page.locator("//input[@id='userName']").fill("Rodrigo")
            login_page.locator("//input[@id='userEmail']").fill("rodrigo@gmail.com")
            login_page.locator("#currentAddress").fill("Dirección uno demo")
            login_page.locator("//textarea[@id='permanentAddress']").fill("Dirección dos permanente demo")

            # Hacer clic en el botón "Submit"
            login_page.locator("//button[@id='submit']").click()

            # Validar la URL después de hacer clic en "Submit"
            expect(login_page).to_have_url(re.compile(".*text-box"))

        locator_buton_submit = "//button[@id='submit']"
        # Llamar a la función para medir el tiempo de carga y validar la presencia del elemento
        measure_load_time(login_page, test_form, locator_buton_submit, 30)
