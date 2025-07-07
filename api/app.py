from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn

modelo = joblib.load('../modelo/modelo_projetos.pkl')

app = FastAPI()

class Projeto(BaseModel):
    duracao: float
    orcamento: float
    equipe: int
    recursos: str
    historico_sucesso: float 

def calcular_limite(historico_sucesso: float) -> float:
    margem = 0.1 
    return historico_sucesso * 100 * (1 - margem)

@app.post("/prever")
def prever(projeto: Projeto):
    recursos_num = {'Baixo': 0, 'Médio': 1, 'Alto': 2}.get(projeto.recursos, 1)

    proba = modelo.predict_proba([[projeto.duracao, projeto.orcamento, projeto.equipe, recursos_num]])[0][1] * 100

    limite = calcular_limite(projeto.historico_sucesso)

    recomendacao = "Viável" if proba >= limite else "Requer ajustes"

    return {
        "probabilidade_sucesso": f"{proba:.1f}%",
        "limite": f"{limite:.1f}%",
        "recomendacao": recomendacao
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)