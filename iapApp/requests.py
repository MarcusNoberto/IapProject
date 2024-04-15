import requests

url = 'http://127.0.0.1:8000/iaps/BlockCraft/setPrice/'
payload = {
    'id': 1,
    'country': 'US',
    'new_price': '3.99'
}
response = requests.post(url, data=payload)

print(response.status_code)
print(response.json())
