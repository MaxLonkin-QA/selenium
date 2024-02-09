"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '9401d31568f76e2fc492f8ad7ff87864'
          }
body1 = {
"name": "Dany",
"photo": "https://dolnikov.ru/pokemons/albums/004.png"
    }
response = requests.post(url=f'{URL}/pokemons',json=body1,headers=HEADER,timeout=5) 
print(response.text, f'Статус кода: {response.status_code}')
parsed1 = response.json()
parsed = parsed1['id']

body2 = {
    "pokemon_id": f"{parsed}",
    "name": "Пура",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
}

body3 = {
    "pokemon_id": f"{parsed}"
}

response = requests.put(url=f'{URL}/pokemons',json=body2,headers=HEADER,timeout=5)
print(response)

response = requests.post(url=f'{URL}/trainers/add_pokeball',json=body3,headers=HEADER,timeout=5)
print(response)

#--alluredir=my_allure_results"