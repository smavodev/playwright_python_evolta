import re
import os
import pytest
from playwright.sync_api import sync_playwright, expect
from Utils.load_time_advanced import measure_load_time
from Config.Config import Config

URL_BASE = "https://demoqa.com/"
BROWSER = "chrome"
RUTA_DATA = os.getenv("RUTA_DATA")
FIRST_NAME = "Rodrigo"
EMAIL = "rodrigo@gmail.com"
ADDRES = "Dirección uno demo"

TIMEOUT = 30


class TestSuccess:

    @pytest.fixture(scope="module")
    def browser(self):
        config = Config(browser=BROWSER, headless=False)
        context = config.get_browser_context()
        yield context
        context.close()

    @pytest.fixture
    def base_test(self, browser):
        page = browser.new_page()
        page.goto(URL_BASE)  # Utiliza el método goto para navegar a la URL base
        yield page
        page.close()

    def test_example_2(self, base_test):

        def registro_test2():
            # Hacer clic en "Elements"
            base_test.locator("text=Elements").click()
            expect(base_test).to_have_url(re.compile(".*elements"))

            # Hacer clic en "Text Box"
            base_test.locator("text=Text Box").click()
            expect(base_test).to_have_url(re.compile(".*text-box"))

        measure_load_time(base_test, registro_test2, "text=Text Box", TIMEOUT)

        def test_form2():
            # Rellenar formularios
            base_test.locator("//input[@id='userName']").fill(FIRST_NAME)
            base_test.locator("//input[@id='userEmail']").fill(EMAIL)
            base_test.locator("#currentAddress").fill(ADDRES)
            base_test.locator("//textarea[@id='permanentAddress']").fill("Dirección dos permanente demo")

            # Hacer clic en el botón "Submit"
            base_test.locator("//button[@id='submit']").click()

            # Validar la URL después de hacer clic en "Submit"
            expect(base_test).to_have_url(re.compile(".*text-box"))

        locator_buton_submit = "//button[@id='submit']"
        measure_load_time(base_test, test_form2, locator_buton_submit, TIMEOUT)
