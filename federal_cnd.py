import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def emitir_cnd_federal():
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--window-size=800,600")
    # Aqui você pode adicionar mais opções se necessário.

    # Inicializar o driver do Chrome usando undetected_chromedriver
    driver = uc.Chrome(options=options)

    # URL da Receita Federal
    url = 'https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/EmitirPGFN'
    
    # Acessar a página
    driver.get(url)
    
    # Encontrar o elemento de input para o CNPJ e inserir o valor
    cnpj_value = "00.412.572/0001-88"
    cnpj_input = driver.find_element(By.ID, "NI")
    cnpj_input.send_keys(cnpj_value)

    # Clicar no botão "Consultar"
    consultar_button = driver.find_element(By.ID, "validar")
    consultar_button.click()
    
    # Aguarde até que o elemento desejado (resultado da consulta) esteja visível
    resultado_consulta_element = WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main-container']/div/table/tbody/tr/td")))
    
    # Obtenha o texto do elemento
    texto_resultado = resultado_consulta_element.text

    # Verificar se o texto contém o CNPJ e a mensagem de "inapta"
    if cnpj_value in texto_resultado and "são insuficientes para a emissão de certidão por meio da Internet." in texto_resultado:
        print("Situação: NHHHHGG")
    else:
        print("Situação: NÃO APTA A CND RFB")
    
    # Por enquanto, apenas manteremos o navegador aberto para visualização
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    emitir_cnd_federal()
