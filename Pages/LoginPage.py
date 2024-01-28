from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url):
        self.page.goto(url)

    def login_success(self, username, password):
        self.page.fill('//*[@id="txtUsuario"]', username)
        self.page.fill('//*[@id="txtClave"]', password)
        self.page.click("//input[contains(@class,'btn btn-lg btn-danger btn-block')]")
        self.page.wait_for_selector("//h2[contains(.,'Enero')]")

    def login_failure(self, username, password):
        self.page.fill('//*[@id="txtUsuario"]', username)
        self.page.fill('//*[@id="txtClava"]', password)
        self.page.click("//input[contains(@class,'btn btn-lg btn-danger btn-block')]")

