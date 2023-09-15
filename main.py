from selenium import webdriver
from time import sleep

class Cookie_game():
    def __init__(self):
        self.abrir_navegador()
        self.abrir_site('https://orteil.dashnet.org/cookieclicker/')
        self.jogar()
        sleep(10)

    def jogar(self):
        while True:
            self.clicar_no_cookie()
    def abrir_navegador(self):
        self.navegador = webdriver.Chrome()

    def abrir_site(self, site):
        self.navegador.get(site)
        sleep(10)
        #Escolher linguagem
        self.navegador.find_element('css selector', 'div#langSelect-PT-BR').click()   

    def clicar_no_cookie(self):
        for x in range(20):
            try:self.navegador.find_element('css selector', 'button#bigCookie').click()
            except Exception as E:
                #print(E)
                pass
Cookie_game()