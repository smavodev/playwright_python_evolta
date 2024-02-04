from playwright.sync_api import Page
from Utils.load_time_basic import measure_load_time


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)

    def login_success_1(self, user_data):
        username = user_data.get("username")
        password = user_data.get("password")
        self.page.fill('//*[@id="txtUsuario"]', username)
        self.page.fill('//*[@id="txtClave"]', password)
        self.page.click("//input[contains(@class,'btn btn-lg btn-danger btn-block')]")
        self.page.wait_for_selector("//div[@class='fc-toolbar fc-header-toolbar']")

    def login_success_2(self, username, password, mes_inicio, tiempo=5):
        def action1():
            self.page.fill('//*[@id="txtUsuario"]', username)
            self.page.fill('//*[@id="txtClave"]', password)
            self.page.click("//input[contains(@class,'btn btn-lg btn-danger btn-block')]")
        selector = "//h2[contains(.,'"+str(mes_inicio)+"')]"
        measure_load_time(self.page, action1, selector, t_espera=tiempo)

    def panelSeguimiento(self, tiempo):
        def action2():
            self.page.locator("//a[contains(.,'Gestión Seguimiento')]").click()
            self.page.locator("//a[contains(.,'Panel de Seguimiento')]").click()

        selector = "//section[@id='divcotizarOcultarFiltroEstado']"
        measure_load_time(self.page, action2, selector, t_espera=tiempo)

    def busquedaLeads(self, busqueda_a, validacion_a, tiempo):
        def action3():
            self.page.locator("//a[@href='#'][contains(.,'Inicio')]").click()
            self.page.locator("//input[contains(@type,'search')]").fill(busqueda_a)
            self.page.locator("//button[contains(.,'Buscar')]").click()

        selector = "//span[contains(.,'"+str(validacion_a)+"')]"
        measure_load_time(self.page, action3, selector, t_espera=tiempo)
