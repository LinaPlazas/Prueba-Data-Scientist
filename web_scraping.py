# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:20:51 2021

@author: linal
"""

from bs4 import BeautifulSoup,Comment
import requests
import pandas as pd
from selenium import webdriver

url="https://play.google.com/store/apps/details?id=com.clarocolombia.miclaro&hl=es_CO&gl=US&showAllReviews=true"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
driver = webdriver.Chrome(r"C:\Users\linal\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

Comentarios_lista1 = []
for el in soup.find_all("span", attrs={'jsname': "bN97Pc"}):
    Comentarios_lista1.append(str(el.get_text()))
   
Comentarios_lista2 = []
for el in soup.find_all("span", attrs={'jsname': "fbQN7e"}):
    Comentarios_lista2.append(str(el.get_text()))
    
Comentarios_lista = Comentarios_lista2 
for i in range(len(Comentarios_lista2)):
    if Comentarios_lista2[i]=="":
        Comentarios_lista[i]=Comentarios_lista1[i]

        
        
Comentarios_lista=pd.DataFrame(Comentarios_lista)
Comentarios_lista.rename({0: 'Comentarios'}, axis=1, inplace=True)
Comentarios_lista.to_excel("Comentarios.xlsx",index=False)
