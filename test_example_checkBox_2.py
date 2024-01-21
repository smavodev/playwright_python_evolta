# playwright codegen  https://demoqa.com/checkbox

import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


def test_checkbox4(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=400)
    # context=browser.new_context(record_video_dir="Videos/Input")
    context = browser.new_context(
        viewport={'width': 1500, 'height': 800}
        # record_video_dir="Videos/Checkbox"
    )
    # Open new page
    page = context.new_page()

    page.goto("https://datatables.net/extensions/select/examples/initialisation/checkbox")
    expect(page).to_have_title("DataTables example - Checkbox selection")
    # Tiempo de Espera
    page.set_default_timeout(5000)

    # Scrholl de la página
    page.mouse.wheel(0, 400)
    time.sleep(2)

    # for i in range (1,11):   #Recuerden el ultimo es para el incremento
    #     page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()

    #     #limite en el 3
    #     if i==3:
    #         page.locator("//a[contains(@data-dt-idx,'2')]").click()
    #     if i==6:
    #         page.locator("//a[contains(@data-dt-idx,'3')]").click()

    #     time.sleep(0.7)

    for i in range(1, 11):  # Recuerden el ultimo es para el incremento
        page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()

        # limite en el 3
        if i == 10:
            page.locator("//a[contains(@data-dt-idx,'2')]").click()
            for x in range(1, 11):
                page.locator(f"(//td[contains(@class,'  select-checkbox')])[{x}]").click()
                if x == 10:
                    page.locator("//a[contains(@data-dt-idx,'3')]").click()
                    for y in range(1, 11):
                        page.locator(f"(//td[contains(@class,'  select-checkbox')])[{y}]").click()
                    page.locator("//input[contains(@type,'search')]").fill("Je")
                    time.sleep(2)
                    page.locator("(//td[contains(@class,'  select-checkbox')])[3]").click()

        time.sleep(0.5)

    # expect(page).to_have_url(re.compile(".*datos-personales/"))
    context.close()
    browser.close()


