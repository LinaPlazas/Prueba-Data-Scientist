# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Fri Jul 23 21:20:51 2021

@author: linal
"""

from bs4 import BeautifulSoup,Comment
import requests
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def connect_url(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    delay = 20 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup
def find_comments(soup):
    Comentarios_lista1 = []
    ## Encuentra los comentarios largos es decir que tienen la opción de mostrar más
    for el in soup.find_all("span", attrs={'jsname': "bN97Pc"}):
        Comentarios_lista1.append(str(el.get_text()))
    ## Encuentra los comentarios cortos
    Comentarios_lista2 = []
    for el in soup.find_all("span", attrs={'jsname': "fbQN7e"}):
        Comentarios_lista2.append(str(el.get_text()))
    ## Deja los comentarios más largos que encuentre
    Comentarios_lista = Comentarios_lista2
    for i in range(len(Comentarios_lista2)):
        if Comentarios_lista2[i]=="":
            Comentarios_lista[i]=Comentarios_lista1[i]
    return Comentarios_lista


if __name__=="__main__":
    ## url de la página a consultar
    url="https://play.google.com/store/apps/details?id=com.clarocolombia.miclaro&hl=es_CO&gl=US&showAllReviews=true"
    ## Esta función  se comunica con el navegador web y espera hasta que este completamente cargado
    soup=connect_url(url)
    ## Esta función encuentra todos los comentarios de la página
    Comentarios_lista=find_comments(soup)
    ## convertir lista de comentarios a dataframe
    Comentarios_lista=pd.DataFrame(Comentarios_lista)
    Comentarios_lista.rename({0: 'Comentarios'}, axis=1, inplace=True)
    ## Exportar comentarios a excel
    #Comentarios_lista.to_excel("Comentarios.xlsx",index=False)
