# JusCashAML

## Estrutura de pastas
```JusCashAML/
JusCashAML/
│
├── modelo/
│   ├── treinamento.py         # Script para treinar o modelo
│   ├── modelo_projetos.pkl    # Arquivo do modelo treinado
│
├── api/
│   ├── app.py                 # Código da API FastAPI
│
├── chatbot/
│   ├── chatbot.py             # Código do chatbot cliente
│   ├── usuarios.json          # Dados dos usuários cadastrados
│
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
```

## Exemplo de Uso:
**Certifique-se de baixar corretamente todos os arquivos do repositório Git e mantê-los na mesma estrutura de pastas.**

### Manualmente:
1. Execute o arquivo de treinamento do modelo (python treinamento.py)
2. Inicie a API (python app.py)
3. Em outro terminal, execute o chatbot (python chatbot.py)
4. Siga as instruções interativas
5. Informe um e-mail cadastrado no usuarios.json
6. Insira os dados do projeto quando solicitado de acordo com as regras de negócios e formatação

### Via terminal

Passo a passo para rodar o projeto no terminal

1. Abra o terminal (cmd, PowerShell, bash, etc).

2. Navegue até a pasta do projeto para treinamento do modelo:  
   Exemplo:  
   cd C:\Users\geiss\JusCashAML\modelo

3. Execute o treinamento do modelo:  
   python treinamento.py

4. Navegue até a pasta da API:  
   Exemplo:  
   cd C:\Users\geiss\JusCashAML\api

5. Inicie a API:  
   python app.py

6. Em outro terminal, navegue até a pasta do chatbot:  
   Exemplo:  
   cd C:\Users\geiss\JusCashAML\chatbot

7. Execute o chatbot:  
   python chatbot.py

   Imagem de auxilio:

   ![image](https://github.com/user-attachments/assets/ab3aae94-7ffd-4b28-ace2-4b809287c817)


Observações:
- Certifique-se de que o Python está instalado e configurado no PATH do sistema.
- Execute os comandos na pasta onde os arquivos estão localizados para evitar erros de "arquivo não encontrado".
- Você pode abrir múltiplos terminais para executar a API e o chatbot simultaneamente.


# Regras de Negócio
## API de Previsão

A API realiza previsões de viabilidade de projetos com base em um modelo de Machine Learning. O usuário deve estar previamente cadastrado no arquivo `usuarios.json`.

### Requisição

A API espera um JSON com os seguintes campos:

- `duracao` (float): duração do projeto em meses.  
- `orcamento` (float): orçamento total do projeto em reais.  
- `equipe` (int): número de pessoas envolvidas no projeto.  
- `recursos` (str): nível de recursos disponíveis. Pode ser "Baixo", "Médio" ou "Alto".  
- `historico_sucesso` (float): percentual de sucesso dos projetos anteriores do usuário (valor entre 0 e 1).  

### Regras de decisão

- Um limite de viabilidade é calculado com base no histórico do usuário, aplicando-se uma margem de 10% (ou seja, limite = histórico × 90%).  
- Se a probabilidade de sucesso prevista pelo modelo for maior ou igual ao limite, o projeto é considerado **Viável**.  
- Caso contrário, é considerado **Requer ajustes**.


## Chatbot Interativo

O chatbot coleta os dados do projeto e envia para a API. A interação ocorre pelo terminal.

### Dados solicitados

- Duração do projeto (em meses)  
- Orçamento (em reais, aceita formatos como `100.500,50` ou `100500.50`)  
- Tamanho da equipe (número inteiro)  
- Nível de recursos: "Baixo", "Médio" ou "Alto"  

### Regras adicionais

- O usuário deve informar um e-mail cadastrado previamente no arquivo `usuarios.json`.  
- O usuário pode digitar `sair` a qualquer momento para interromper o processo.  
- Se o usuário possuir projetos anteriores bem-sucedidos:
  - O sistema calcula o orçamento médio desses projetos.
  - Se o orçamento atual estiver abaixo da média, o chatbot alerta sobre isso.
  - Também compara a previsão atual com o histórico do usuário e emite uma recomendação baseada nessa comparação.  


## Versões das Bibliotecas 
Contidos em requirements.txt
