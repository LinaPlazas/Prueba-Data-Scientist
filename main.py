from fastapi import FastAPI
import uvicorn
import json

## Inicializar Aplicación
app=FastAPI(debug=True)

## Leer Json obtenido en el analisis de sentimientos
f=open("Resultados_comentarios.json",encoding='utf-8')
comentarios=json.load(f)

## Leer el Query dado por el usuario y mostrar solo la cantidad de comentarios indicada
@app.get("/")
async def get_comentarios(número_comentarios):
    comentarios1=[]
    try:
        for i in range(int(número_comentarios)):
            comentarios1.append(comentarios[i])
        json.dumps(comentarios1)
        return comentarios1
    except:
        return "Número de comentarios invalido"

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port="8000")
