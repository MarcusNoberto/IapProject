import requests
import json

url = 'http://127.0.0.1:8000/iaps/BattleTanks/setPrice/'
payload = {
    'id': "com.fungames.battletanksbeta.hardpack5.coupon30usd",
    'country': 'DZ',
    'new_price': '50.44'
}

response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print(response.json())
else:
    print(f"Erro: {response.status_code}")