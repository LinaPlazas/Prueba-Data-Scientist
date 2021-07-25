# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:41:19 2021

@author: linal
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
import pandas as pd

comentarios=pd.read_excel("Comentarios.xlsx")
comentarios["Calificación"]=0.0
for i in range(len(comentarios)):
    text=comentarios["Comentarios"][i]

    nltk.download('vader_lexicon')
    nltk.download('punkt')
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')

    analizador = SentimentIntensityAnalyzer()
    resultados=analizador.polarity_scores(text)
    comentarios["Calificación"][i]=resultados["compound"]


labels = ['1 estrella','2 estrellas', '3 estrellas', '4 estrellas', '5 estrellas']

#create a new column for the age group
comentarios['Estrellas'] = pd.cut(comentarios["Calificación"], bins=5, labels=labels)
comentarios['Sentimiento']=""
for i in range(len(comentarios)):
    if comentarios["Estrellas"][i]=='5 estrellas' or  comentarios["Estrellas"][i]=='4 estrellas':
        comentarios['Sentimiento'][i]="Positivo"
    elif comentarios["Estrellas"][i]=='3 estrellas':
        comentarios['Sentimiento'][i]="Neutro"
    else:
        comentarios['Sentimiento'][i]="Negativo"
comentarios.to_excel("Resultados_comentarios.xlsx",index=False)
