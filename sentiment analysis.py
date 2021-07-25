# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:41:19 2021

@author: linal
"""

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
import six
import os
## importar credenciales de google
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'claves.json'
import pandas as pd

def get_score(text):
    ##Obtiene un score en forma de número que indica que tan positivo o negativo fue el comentario
    client = language_v1.LanguageServiceClient()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    return sentiment.score

def get_stars(comentarios):
    labels = ['1 estrella','2 estrellas', '3 estrellas', '4 estrellas', '5 estrellas']
    comentarios['Estrellas'] = pd.cut(comentarios["Calificación"], bins=5, labels=labels)
    return comentarios

def get_sentiment(comentarios):
    comentarios['Sentimiento']=""
    for i in range(len(comentarios)):
        if comentarios["Estrellas"][i]=='5 estrellas' or  comentarios["Estrellas"][i]=='4 estrellas':
            comentarios['Sentimiento'][i]="Positivo"
        elif comentarios["Estrellas"][i]=='3 estrellas':
            comentarios['Sentimiento'][i]="Neutro"
        else:
            comentarios['Sentimiento'][i]="Negativo"


if __name__=="__main__":
    ## leer dataframe previamente creado en el web scrapping
    comentarios=pd.read_excel("Comentarios.xlsx")
    ## Itera sobre cada comentario para obtener la Calificación con el analisis de sentimientos de google
    comentarios["Calificación"]=0.0
    for i in range(len(comentarios)):
        text=comentarios["Comentarios"][i]
        score= get_score(text)
        comentarios["Calificación"][i]=score
    ## Obtiene estrellas con ayuda de la libreria cut para volver una variable continua en categorica
    comentarios=get_stars(comentarios)
    ## A partir de las estrellas obtenidas, identificar si el comentario fue positivo, negativo o neutro
    get_sentiment(comentarios)
    comentarios.to_excel("Resultados_comentarios.xlsx",index=False)
    comentarios.to_json('Resultados_comentarios.json',orient="records", force_ascii=False)
