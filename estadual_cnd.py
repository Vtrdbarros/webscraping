import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium_stealth import stealth

def emitir_cnd_estadual():
    options = uc.ChromeOptions()
    options.headless = False

    # Inicializar o driver do Chrome usando undetected_chromedriver
    driver = uc.Chrome(options=options)
    driver.set_window_size(800, 600)

    # URL da Receita Estadual de Pernambuco
    url = 'https://efisco.sefaz.pe.gov.br/sfi_trb_gpf/PREmitirCertidaoNegativaNarrativaDebitoFiscal'
    
    # Acessar a página
    driver.get(url)

    # Aguarde até que o dropdown esteja visível
    dropdown_element = WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.ID, "cdTipoDocumento")))
    
    # Selecionar a opção "CNPJ" no dropdown
    select = Select(dropdown_element)
    select.select_by_visible_text("CNPJ")

    # Encontrar o campo de texto do CNPJ e inserir o valor
    cnpj_input = driver.find_element(By.ID, "nuDocumento")
    cnpj_input.send_keys("00.412.572/0001-88")

    # Resolver o reCAPTCHA (você precisará adicionar o código para resolver o reCAPTCHA aqui)
    # o captcha é resolvido automaticamente pelo selenium_stealth ele fica aqui (<div class="recaptcha-checkbox-border" role="presentation"></div>)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    # inicializa o driver selenium_stealth
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
        """
    })

    # Por enquanto, apenas manteremos o navegador aberto para visualização
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

if __name__ == "__main__":
    emitir_cnd_estadual()
