from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def open_browser(site):
    try:
        service = Service()
        options = Options()
        options.add_argument("--log-level=2")
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(site)

        return driver
    except Exception as expt:
        print(f"Erro ao abrir o navegador: {expt}")

def pesquisar_notebooks(driver):
    try:
        driver.implicitly_wait(5)
        search_input = driver.find_element(By.ID, 'input-search')
        search_input.send_keys('notebooks')
        search_input.send_keys(u'\ue007')
        print('Pesquisa por "notebooks" realizada com sucesso!')
    except Exception as expt:
        print(f"Erro ao realizar a pesquisa: {expt}")

def aceitar_cookies(driver):
    try:
        accept_button = driver.find_element(By.CLASS_NAME, 'cc-btn')
        accept_button.click()
        print("Cookies aceitos com sucesso!")
    except Exception as expt:
        print(f"Erro ao aceitar os cookies:")
