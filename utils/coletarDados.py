from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException

def coletar_dados(driver, num_paginas):
    produtos_com_avaliacoes_links = []

    for pagina in range(num_paginas):
        print(f"Coletando dados da página {pagina + 1}...")

        
        #tentativa de coletar os dados da página se der o erro staleElementReference ele tenta novamente 
        try:
            pesquisar_nome = driver.find_elements(By.XPATH, '//h2[@data-testid="product-title"]')
            nomes_produtos = [title.text for title in pesquisar_nome]
        except StaleElementReferenceException:
            pesquisar_nome = driver.find_elements(By.XPATH, '//h2[@data-testid="product-title"]')
            nomes_produtos = [title.text for title in pesquisar_nome]

        try:
            pesquisar_avaliacoes = driver.find_elements(By.XPATH, '//span[@format="score-count"]')
            avaliacoes_produtos = [avaliacao.text for avaliacao in pesquisar_avaliacoes]
        except StaleElementReferenceException:
            pesquisar_avaliacoes = driver.find_elements(By.XPATH, '//span[@format="score-count"]')
            avaliacoes_produtos = [avaliacao.text for avaliacao in pesquisar_avaliacoes]

        try:
            pesquisar_links = driver.find_elements(By.XPATH, '//a[@data-testid="product-card-container"]')
            links_produtos = [link.get_attribute("href") for link in pesquisar_links]
        except StaleElementReferenceException:
            pesquisar_links = driver.find_elements(By.XPATH, '//a[@data-testid="product-card-container"]')
            links_produtos = [link.get_attribute("href") for link in pesquisar_links]


        #combina os dados coletados em um único dataframe
        produtos_com_avaliacoes_links.extend(list(zip(nomes_produtos, avaliacoes_produtos, links_produtos)))


        #tentativa para passar de página 
        try:
            clicar_botao_next = driver.find_element(By.XPATH, '//button[@type="next"]')
            if "disabled" in clicar_botao_next.get_attribute("class"):
                print("Última página alcançada.")
                break

            driver.execute_script("arguments[0].scrollIntoView(true);", clicar_botao_next)
            time.sleep(1)
            clicar_botao_next.click()
            time.sleep(3)
        except (NoSuchElementException, ElementClickInterceptedException):
            print("Não há mais páginas disponíveis ou o botão não está interativo.")
            break

    return produtos_com_avaliacoes_links

#coloquei alguns time.speep para evitar erros (não sei se estão nos melhras lugares