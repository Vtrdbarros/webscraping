from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def puxar_inscricao_estadual_sefaz_pe(cnpj):
    # Configurações do webdriver
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)

    # Acessa a página
    url = 'https://efisco.sefaz.pe.gov.br/sfi_trb_gcc/PREmitirDIAC'
    driver.get(url)

    # Aguarda até que o dropdown esteja visível
    wait = WebDriverWait(driver, 200)
    select_element = wait.until(EC.visibility_of_element_located((By.ID, "primeiro_campo")))

    # Seleciona a opção "CNPJ"
    Select(select_element).select_by_visible_text("CNPJ")

    # Insere o CNPJ
    cnpj_input = driver.find_element(By.ID, "NuDocumentoIdentificacao")
    cnpj_input.send_keys(cnpj)

    # Clica no botão "Localizar"
    localizar_button = driver.find_element(By.ID, "btt_localizar")
    localizar_button.click()

    # Aguarda até que o elemento desejado na tabela esteja visível com o CNPJ
    cnpj_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(), '{cnpj}')]")))
    
    # Pega o elemento anterior que é a Inscrição Estadual
    ie_element = cnpj_element.find_element(By.XPATH, "./preceding-sibling::td[1]")

    # Fecha o navegador
    driver.quit()

    # Retorna o valor da Inscrição Estadual
    return ie_element.text

# Teste da função
cnpj_teste = "00.412.572/0001-88"
inscricao_estadual = puxar_inscricao_estadual_sefaz_pe(cnpj_teste)
print(f"A Inscrição Estadual para o CNPJ {cnpj_teste} é: {inscricao_estadual}")
