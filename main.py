from fastapi import FastAPI
import uvicorn
import json

app=FastAPI(debug=True)
f=open("Resultados_comentarios.json",encoding='utf-8')
comentarios=json.load(f)



@app.get("/")
async def get_comentarios(n_comentarios):
    comentarios1=[]
    for i in range(int(n_comentarios)):
        comentarios1.append(comentarios[i])
    json.dumps(comentarios1)
    return comentarios1

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port="8000")
