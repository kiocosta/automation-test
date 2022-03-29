import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:/botwhatsapp/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://web.whatsapp.com/')
time.sleep(10)
contatos = ['Renanminiskov']



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

    for i in range (2, 5):
        pacote_figurinha = driver.find_element_by_xpath('//body//div[@id='app']//footer//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[2]')
        pacote_figurinha.click()
        time.sleep(3)

        for i in range(1, 90):
            figurinha = driver.find_element_by_xpath('//body//div[@id='app']//footer//div//div//div//div//div[2]//div[1]//div[1]//div[' + i +']')
            figurinha.click()

for contato in contatos:
    buscar_contato(contato)
    enviar_figurinha()