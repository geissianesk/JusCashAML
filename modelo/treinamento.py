# Importações
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

dados = {
    'Duração': [6, 12, 9, 4, 8, 10],
    'Orçamento': [500000, 1000000, 750000, 300000, 600000, 900000],
    'Equipe': [10, 15, 8, 5, 9, 12],
    'Recursos': ['Alto', 'Médio', 'Baixo', 'Baixo', 'Médio', 'Alto'],
    'Sucesso': [1, 0, 1, 0, 1, 1]
}
df = pd.DataFrame(dados)

df['Recursos'] = df['Recursos'].map({'Baixo': 0, 'Médio': 1, 'Alto': 2})

X = df[['Duração', 'Orçamento', 'Equipe', 'Recursos']]
y = df['Sucesso']
modelo = RandomForestClassifier().fit(X, y)

joblib.dump(modelo, 'modelo_projetos.pkl')
print("Modelo treinado e salvo!")