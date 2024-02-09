import requests
import pytest
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '9401d31568f76e2fc492f8ad7ff87864'
         }
def test_get_trainers():
    """
    KTI-1. get_trainers_by_id
    """
    response = requests.get(url=f'{URL}/pokemons', params={'trainers_id':3470},headers=HEADER,timeout=5) 
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainer():
    """
    KTI-2. get_trainer_name
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3470},headers=HEADER,timeout=5) 
    assert response.json()['trainer_name'] == 'Мистермикс', ''

  