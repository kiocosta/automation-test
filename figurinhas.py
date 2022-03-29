import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:/botwhatsapp/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://web.whatsapp.com/')
time.sleep(10)
print('ok')
contatos = ['Renanminiskov']
mensagem = 'eae véi'

def buscar_contato(contato):
    print(contato)
    campo_pesquisa = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1awRl", " " ))]');
    print(campo_pesquisa)
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_figurinha():
    icone_emoji = driver.find_element_by_xpath('//*[contains(@class, "nw8RZ _1isZ2")]')
    icone_emoji.click()
    time.sleep(3)
    aba_figurinha = driver.find_element_by_xpath('//button[contains(concat(" ",normalize-space(@class)," ")," _37evB ")][contains(concat(" ",normalize-space(@class)," ")," _16P6V ")][contains(concat(" ",normalize-space(@class)," ")," _3x5p4 ")][contains(concat(" ",normalize-space(@class)," ")," _3guyl ")]')
    aba_figurinha.click()
    time.sleep(7)
    pacote_figurinha = driver.find_element_by_xpath('//**[contains(concat( " ", @class, " " ), concat( " ", "_1zlQ1", " " )) and (((count(preceding-sibling::) + 1) = 4) and parent::**)]//[contains(concat( " ", @class, " " ), concat( " ", "_1VzZY", " " ))]')
    pacote_figurinha.click()
    time.sleep(3)
    figurinha = driver.find_element_by_xpath('//**([contains(concat( " ", @class, " " ), concat( " ", "_2elZc", " " )) and (((count(preceding-sibling::**) + 1) = 5) and parent::**)]//**[contains(concat( " ", @class, " " ), concat( " ", "_2YpcJ", " " ))]')
    figurinha.click()

for contato in contatos:
    buscar_contato(contato)
    enviar_figurinha()