from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

print("Iniciando script...")

# Configurações do webdriver
options = webdriver.ChromeOptions()
options.headless = False
print("Configurações do WebDriver definidas.")

driver = webdriver.Chrome(options=options)
print("Driver do Chrome iniciado.")

# Acessa a página
url = 'https://efisco.sefaz.pe.gov.br/sfi_trb_gcc/PREmitirDIAC'
print(f"Acessando a página: {url}")
driver.get(url)

# Aguarda até que o dropdown esteja visível
wait = WebDriverWait(driver, 200)
select_element = wait.until(EC.visibility_of_element_located((By.ID, "primeiro_campo")))

# Seleciona a opção "CNPJ"
Select(select_element).select_by_visible_text("CNPJ")

# Insere o CNPJ
cnpj_input = driver.find_element(By.ID, "NuDocumentoIdentificacao")
cnpj_input.send_keys("00.412.572/0001-88")

# Clica no botão "Localizar"
localizar_button = driver.find_element(By.ID, "btt_localizar")
localizar_button.click()

# Aguarda até que o elemento desejado na tabela esteja visível com o CNPJ
cnpj_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), '00.412.572/0001-88')]")))
# Pega o elemento anterior que é a Inscrição Estadual
ie_element = cnpj_element.find_element(By.XPATH, "./preceding-sibling::td[3]")

# Imprime o valor do elemento
print(f"A Inscrição Estadual é: {ie_element.text}")

# Mantém o script rodando para que o navegador não feche
while True:
    time.sleep(100)
