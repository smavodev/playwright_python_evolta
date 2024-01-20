from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://test.evolta.pe/Login/Acceso/Index")
    page.get_by_placeholder("Usuario").click()
    page.get_by_placeholder("Usuario").press("CapsLock")
    page.get_by_placeholder("Usuario").fill("w")
    page.get_by_placeholder("Usuario").press("CapsLock")
    page.get_by_placeholder("Usuario").fill("wCORTEZ")
    page.get_by_placeholder("Usuario").press("Tab")
    page.get_by_placeholder("Contraseña").press("Control+V")
    page.get_by_role("button", name="Acceder").click()
    page.get_by_role("link", name=" Gestión Seguimiento ").click()
    page.goto("https://test.evolta.pe/Graficos/Dashborad/IndexDashBoard")
    page.get_by_role("link", name=" Inicio").click()
    page.get_by_placeholder("Ingresar correo, DNI, nombres").click()
    page.get_by_placeholder("Ingresar correo, DNI, nombres").fill("GMAIL")
    page.get_by_role("button", name=" Buscar").click()
    page.get_by_role("link", name=" Buscar Prospectos").click()
    page.get_by_role("button", name=" Buscar").click()
    page.get_by_role("link", name=" ").click()
    page.get_by_role("link", name="Salir").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
