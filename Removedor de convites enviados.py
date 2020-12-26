#   Importa bibliotecas de manipulação web
print("Importando libs")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

#   Tela inicial
os.system('cls')
print("""*-------------------------------------------------------------------------------*
ATENÇÃO!
    Você está prestes a utilizar um robô no Linkedin.
    Nenhum dado aqui será armazenado, sendo assim, o desenvolvedor está distante de qualquer responsabilidade envolvendo seu perfil.
    Você ao utilizar esse script, está ciente de que é o único responsável pelo seu perfil e sua máquina.

A SEGUIR:
    Será solicitado e-mail e senha utilizados no LINKEDIN para poder realizar acesso.
    Assim que o login for realizado, os dois inputs serão destruidos da memória do seu computador, sendo assim, fica claro meu desinteresse pelos seus dados pessoais.
    Esse script entra na página de convites enviados e retira todos os pedidos SEM CRITÉRIO ALGUM, caso deseje finaliza-lo, basta encerrar o terminal.

OBSERVAÇÃO:
    No final da consulta, será aberto a tela do feed sugerindo uma mensagem de agradecimento ao desenvolvedor, peço encarecidamente que publique.
    Recomendações podem ser feitas no perfil do desenvolvedor através do link a seguir:
        https://www.linkedin.com/in/joão-gabriel-maciel-288637163/

Um abraço!
    João Gabriel, Analista de Dados.
*-------------------------------------------------------------------------------*
\a""")

#   Solicita login e senha
validado: bool = False
while not validado:
    print("A seguir informe seu...")
    login = input(" e-mail:   ").strip()
    senha = input(" senha:    ").strip()

    if len(senha) >= 8:
        validado = True


#   Inicia o manipulador
print("\nAbrindo navegador...")
driver = webdriver.Firefox()

#   Vai até o login
print("Indo até o site de login...")
site_login = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fmynetwork%2Finvitation-manager%2Fsent%2F&fromSignIn=true&trk=cold_join_sign_in"
driver.get(site_login)
time.sleep(1)

#   Entra na conta
print("Digitando login...")
driver.find_element_by_id("username").send_keys(login)

print("Digitando senha...")
driver.find_element_by_id("password").send_keys(senha)

print("Confirmando...")
driver.find_element_by_id("password").send_keys(Keys.ENTER)
time.sleep(3)

#   Valida se ainda está na tela de login
print("Validando a confirmação do login...")
if driver.current_url == site_login:
    print("Erro no login")
    exit()

#   Vai até o site
print("Indo até o site de solicitações...\n")
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
time.sleep(1)

#   Conta a quantidade de pessoas
print("Realizando contagem de pessoas...")
cont_pessoas = int(driver.find_element_by_class_name("artdeco-pill__text").text.replace("Pessoas (", "").replace(")", ""))+3
print(f"Quantidade de pessoas: {cont_pessoas}")

try:
    #   Captura todas as pessoas da tela
    for i in range(cont_pessoas):
        print(f"\nIniciando etapa {i+1} de {cont_pessoas}...")
        retirar = driver.find_elements_by_class_name("artdeco-button__text")[i]
        print(retirar.text)
        try:
            if retirar.text.strip() == "Retirar":
                retirar.click()
                driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                print("O clique foi bem sucedido!")
        except:
            print("O clique não foi bem sucedido!")

        time.sleep(0.5)

    #   Monta string de agradecimento
    agradecimento = """
Você tem muitos convites enviados pendentes e está sem tempo para remove-los?
Pois saiba que eu acabo de remover TODOS os meus convites enviados com um simples clique!

Tudo isso foi possível graças ao script do João Gabriel.
Vale a pena dar uma olhada ;)

É possível solicitar o script em Python através de:
    Linkedin: https://www.linkedin.com/in/jo%C3%A3o-gabriel-maciel-288637163/
    WhatsApp: +55 15 99109-6245

#python #selenium #helloworld #rpa #automatizacao #automacao #gratidao
"""

    #   Vai até o feed
    site_feed = "https://www.linkedin.com/feed/"
    driver.get(site_feed)

    #   Clica em começar uma publicação
    try:
        for botao in driver.find_elements_by_tag_name("button"):
            if botao.text.strip() == "Começar publicação":
                botao.click()
                time.sleep(0.25)
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]").send_keys(agradecimento)
    except:
        True

finally:
    cont_pessoas = None
    driver = None
    retirar = None
    input("\a\nROTINA FINALIZADA...")
    os.system('cls')