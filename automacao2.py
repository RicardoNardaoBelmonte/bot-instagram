from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

def iniciar_driver():
    # Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=1000,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    # Navegar até um site
    return driver, wait

driver, wait = iniciar_driver()

driver.get('https://www.instagram.com/')

campo_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
campo_usuario.send_keys('')
sleep(5)

campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
campo_senha.send_keys('')
sleep(5)

botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//div[text()="Entrar"]')))
sleep(3)

botao_entrar.click()
sleep(10)
while True:
    driver.get('https://www.instagram.com/nike/')
    sleep(5)
    postagens = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagu']")))
    postagens[0].click()
    sleep(5)
    try:
        botao_like = driver.find_element(By.XPATH, '//section//div[@role="button"]//*[@aria-label="Curtir"]')
    except:
        print('Imagem já esta Curtida!')
    else:
        botao_like_clicar  = botao_like.find_elements(By.XPATH, '//article[@role="presentation"]//section//div[@role="button"]')
        sleep(3)
        driver.execute_script('arguments[0].click()', botao_like_clicar[0])
        print('Postagem Curtida')
    sleep(86400)
    
