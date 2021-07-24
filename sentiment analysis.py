# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 08:41:19 2021

@author: linal
"""

from google.cloud import language_v1
#from google.cloud.language_v1 import enums
#from google.cloud.language_v1 import types

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\linal\OneDrive\Documents\Prueba_Data_Scientist\Prueba-Data-Scientist\claves.json'
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Hello, world!"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment


import nltk
from googletrans import Translator
import re,string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
translations = translator.translate("Desde hace un año que compré éste paquete, ha sido un desperdicio de dinero, el 80% del supuesto servicio siempre estaba sin señal y eso que tenía un sólo aparato conectado. Tener hogar claro y a la vez claro post pago, el último señalado se atiene al primero y viceversa, en total post pago baja su calidad de servicio; dicho ésto, solicito la desconexión inmediata de claro hogar")
translations =re.sub('[%s]' % re.escape(string.punctuation), ' ', translations.text )


#for translation in translations:
#    print(translation.origin, ' -> ', translation.text)
    
nltk.download('vader_lexicon')
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
sentences = tokenizer.tokenize(translations)

analizador = SentimentIntensityAnalyzer()


for sentence in sentences:
    print(sentence)
    scores = analizador.polarity_scores(sentence)
    for key in scores:
        print(key, ': ', scores[key])
        print()