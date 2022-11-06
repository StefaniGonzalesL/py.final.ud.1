import requests

url="https://pokeapi.co/api/v2/"
peticion=requests.get(url)
datos_json=peticion.json()
for k,v in datos_json.items():
    print(f"{k}: {v}")

