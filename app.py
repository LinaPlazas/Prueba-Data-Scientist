from fastapi import FastAPI
import uvicorn
import json
import pandas as pd
app=FastAPI(debug=True)
f=open("Resultados_comentarios.json",encoding='utf-8')
comentarios=json.load(f)



@app.get("/")
async def get_comentarios(n_comentarios):
    comentarios1=pd.DataFrame()
    for i in range(int(n_comentarios)):
        comentarios1=comentarios1.append(comentarios[i],ignore_index=True)
    result = comentarios1.to_json(orient="records")
    result = json.loads(result)
    json.dumps(result, indent=4)
    return result

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port="8000")
