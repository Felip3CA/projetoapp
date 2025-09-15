import requests
url = "https://api.adviceslip.com/advice"

resposta = requests.get(url)
print("teste prof")
if resposta.status_code == 200:
    dados = resposta.json()
    conselho = dados['slip']['advice']
    print("💡 Conselho do dia:", conselho)
else:
    print("Erro:", resposta.status_code, resposta.text)


APP_ID = "e0648809"
APP_KEY = "197ccb154919c7c526bdb8a201b34a7c"

url = "https://api.edamam.com/api/nutrition-data"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "ingr": "1 large apple"
}

resposta = requests.get(url, params=params)

if resposta.status_code == 200:
    dados = resposta.json()
    print("Calorias:", dados.get("calories"))
    print("Peso total:", dados.get("totalWeight"))
    print("Nutrientes:", dados.get("totalNutrients"))
else:
    print("Erro:", resposta.status_code, resposta.text)