# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:32:55 2021

@author: linal
"""


from fastapi import FastAPI
import uvicorn
import json

app=FastAPI(debug=True)

datos={"1":"python","2":"java","3":"JAVASCRIPT"}

@app.get("/")
def raiz():
    sincodificar=json.dumps(datos)
    return json.loads(sincodificar)
if __name__== '__main__':
    uvicorn.run(app,port=9090)
