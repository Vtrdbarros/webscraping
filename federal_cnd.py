import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import logging

# Configurar o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# Função para emitir a CND Federal

def emitir_cnd_federal(cnpj_value):
    logging.info("Iniciando CND Federal...")
    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--window-size=800,600")

    # Inicializar o driver do Chrome usando undetected_chromedriver
    driver = uc.Chrome(options=options)

    # URL da Receita Federal
    url = 'https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/EmitirPGFN'
    
    # Acessar a página
    logging.info("Acessando a página da Receita Federal...")
    driver.get(url)
    
    # Encontrar o elemento de input para o CNPJ e inserir o valor
    cnpj_input = driver.find_element(By.ID, "NI")
    cnpj_input.send_keys(cnpj_value)
    logging.info(f"Inserindo o CNPJ: {cnpj_value}")

    # Clicar no botão "Consultar"
    consultar_button = driver.find_element(By.ID, "validar")
    consultar_button.click()
    logging.info("Clicando no botão 'Consultar'")

    try:
        # Aguarde até que o elemento desejado (resultado da consulta) esteja visível OU um erro específico seja encontrado
        resultado_consulta_element = WebDriverWait(driver, 200).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='main-container']/div/table/tbody/tr/td"
))
        )
        logging.info("Resultado da consulta encontrado!")   
        texto_resultado = resultado_consulta_element.text

        if 'insuficiente' in texto_resultado.lower():
            logging.info("Situação: NHHHHGG")
            screenshot = driver.get_screenshot_as_png()
            with open("screenshot.png", "wb") as f:
                f.write(screenshot)
        else:
            logging.info("Situação: NÃO encontrado")
        
    except Exception as e:
        logging.error(f"Erro ao tentar obter resultado da consulta: {e}")
    
    # Por enquanto, apenas manteremos o navegador aberto para visualização
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

def consultar_cnd():
    cnpj_value = cnpj_entry.get()
    emitir_cnd_federal(cnpj_value)

# cria a função start.gui
def start_gui():
    global cnpj_entry, root

    # Criar a janela Tkinter
    root = tk.Tk()
    root.title("Consulta de CNPJ")

    # Adicionar entrada para o CNPJ
    cnpj_label = tk.Label(root, text="Informe o CNPJ:")
    cnpj_label.pack()

    cnpj_entry = tk.Entry(root)
    cnpj_entry.pack()

    # Botão para acionar a consulta
    consultar_button = tk.Button(root, text="Consultar CNPJ", command=consultar_cnd)
    consultar_button.pack()

    # Iniciar a janela Tkinter
    root.mainloop()


if __name__ == "__main__":
    start_gui()