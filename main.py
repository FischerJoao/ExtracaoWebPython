from utils.abrirNavegador import open_browser, pesquisar_notebooks, aceitar_cookies
from utils.coletarDados import coletar_dados
from utils.criarExcel import processar_dados
from utils.enviarEmail import enviar_email
import time

def main():
    driver = open_browser("https://www.magazineluiza.com.br/")
    driver.implicitly_wait(6)

    aceitar_cookies(driver)
    time.sleep(2)

    pesquisar_notebooks(driver)
    time.sleep(3)

##escolhe o numero de pags
    num_paginas = 4
    dados = coletar_dados(driver, num_paginas)

    processar_dados(dados)
    driver.quit()

    enviar_email()

if __name__ == "__main__":
    main()
