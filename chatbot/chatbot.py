import json
import requests
from pathlib import Path

CAMINHO_USUARIOS = Path(__file__).parent / "usuarios.json"
API_URL = "http://localhost:8000/prever"

def carregar_usuarios():
    with open(CAMINHO_USUARIOS, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalizar_orcamento(texto):
    texto = texto.strip()
    texto = ''.join(c for c in texto if c.isdigit() or c in [',', '.'])

    if ',' in texto and '.' in texto:
        texto = texto.replace('.', '').replace(',', '.')
    elif ',' in texto:
        texto = texto.replace(',', '.')
    return float(texto)


def pedir_input(mensagem, opcoes=None, tipo=str):
    while True:
        valor = input(mensagem).strip()
        if valor.lower() == 'sair':
            return None
        try:
            valor_convertido = tipo(valor)
            if opcoes and valor_convertido not in opcoes:
                print(f"Valor inválido. Opções válidas: {opcoes}")
                continue
            return valor_convertido
        except:
            print("Entrada inválida, tente novamente.")

def chatbot():
    usuarios = carregar_usuarios()
    
    while True:
        email = input("Digite seu e-mail (ou 'sair'): ").strip().lower()
        if email == 'sair':
            print("Até mais!")
            return
        if email in usuarios:
            usuario = usuarios[email]
            print(f"\nOlá, {usuario['nome']} ({usuario['cargo']})!")
            break
        print("Usuário não encontrado, tente novamente.")

    while True:
        print("\nInforme os dados do projeto (ou 'sair' para cancelar):")

        duracao = pedir_input("Duração (meses): ", tipo=float)
        if duracao is None: break

        orcamento_str = pedir_input("Orçamento (ex: 100.500,50 ou 100500.50): ", tipo=str)
        if orcamento_str is None: break
        try:
            orcamento = normalizar_orcamento(orcamento_str)
        except:
            print("Orçamento inválido.")
            continue

        equipe = pedir_input("Tamanho da equipe: ", tipo=int)
        if equipe is None: break

        recursos = pedir_input("Nível de recursos (Baixo/Médio/Alto): ", opcoes=["Baixo", "Médio", "Alto"])
        if recursos is None: break

        historico = usuario.get('historico_sucesso')

        dados_api = {
            "duracao": duracao,
            "orcamento": orcamento,
            "equipe": equipe,
            "recursos": recursos,
            "historico_sucesso": historico
        }

        try:
            resposta = requests.post(API_URL, json=dados_api).json()
            prob_api = float(resposta['probabilidade_sucesso'].replace('%', '')) / 100
        except Exception as e:
            print(f"Erro ao acessar a API: {e}")
            continue

        print("\nResultado da análise:")
        print(f"Chance pelo modelo: {prob_api*100:.1f}%")

        if historico is not None:
            print(f"Seu histórico de sucesso: {historico*100:.1f}%")
            if prob_api < historico:
                print("Modelo prevê chance menor que seu histórico, avalie o projeto.")
            else:
                print("Modelo prevê chance maior que seu histórico, aproveite!")


        projetos_sucesso = [p for p in usuario.get('projetos_anteriores', []) if p['sucesso']]
        if projetos_sucesso:
            orcamento_medio = sum(p['orcamento'] for p in projetos_sucesso) / len(projetos_sucesso)
            print(f"Orçamento médio dos seus projetos bem-sucedidos: R${orcamento_medio:,.2f}")
            if orcamento < orcamento_medio:
                print("Seu orçamento está abaixo da média dos projetos bem-sucedidos.")

        if input("\nDeseja realizar outra análise? (s/n): ").strip().lower() != 's':
            break

if __name__ == "__main__":
    chatbot()
