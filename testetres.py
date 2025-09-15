import requests

url = "https://api.adviceslip.com/advice"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    conselho = dados['slip']['advice']
    print("💡 Conselho do dia:", conselho)
else:
    print("Erro:", resposta.status_code, resposta.text)