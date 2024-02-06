from playwright.sync_api import Page
from Utils.load_time_advanced_screenshot import measure_load_time


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)

    def login_success_(self, username, password, mes_inicio, tiempo=5):
        def login_success():
            self.page.fill('//*[@id="txtUsuario"]', username)
            self.page.fill('//*[@id="txtClave"]', password)
            self.page.click("//input[contains(@class,'btn btn-lg btn-danger btn-block')]")
        selector = "//h2[contains(.,'"+str(mes_inicio)+"')]"
        measure_load_time(self.page, login_success, selector, t_espera=tiempo, fNumber=1, folder=True)

    def panelSeguimiento_(self, tiempo):
        def panelSeguimiento():
            self.page.locator("//a[contains(.,'Gestión Seguimiento')]").click()
            self.page.locator("//a[contains(.,'Panel de Seguimiento')]").click()

        selector = "//section[@id='divcotizarOcultarFiltroEstado']"
        measure_load_time(self.page, panelSeguimiento, selector, t_espera=tiempo, fNumber=2, folder=True)

    def busquedaLeads_(self, busqueda_a, validacion_a, tiempo):
        def busquedaLeads():
            self.page.locator("//a[@href='#'][contains(.,'Inicio')]").click()
            self.page.locator("//input[contains(@type,'search')]").fill(busqueda_a)
            self.page.locator("//button[contains(.,'Buscar')]").click()

        selector = "//span[contains(.,'"+str(validacion_a)+"')]"
        measure_load_time(self.page, busquedaLeads, selector, t_espera=tiempo, fNumber=3, folder=True)
