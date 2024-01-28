from playwright.sync_api import sync_playwright


class Config:
    def __init__(self, browser, headless=True):
        self.browser_type = browser
        self.headless = headless

    def get_browser_context(self):
        if self.browser_type == 'chrome':
            return sync_playwright().start().chromium.launch(headless=self.headless, slow_mo=1000)
        elif self.browser_type == 'firefox':
            return sync_playwright().start().firefox.launch(headless=self.headless, slow_mo=1000)
        elif self.browser_type == 'webkit':
            return sync_playwright().start().webkit.launch(headless=self.headless, slow_mo=1000)
        else:
            raise ValueError('Invalid browser specified')

