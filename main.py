from selenium import webdriver
from time import sleep

class Cookie_game():
    def __init__(self):
        self.abrir_navegador()
        self.abrir_site('https://orteil.dashnet.org/cookieclicker/')
        sleep(10)

    def abrir_navegador(self):
        self.navegador = webdriver.Chrome()

    def abrir_site(self, site):
        self.navegador.get(site)
        sleep(10)
    