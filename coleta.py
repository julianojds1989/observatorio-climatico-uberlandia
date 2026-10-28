import requests
import json
import os

os.makedirs("dados", exist_ok=True)

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": -18.9186,
    "longitude": -48.2772,
    "start_date": "2025-09-01",
    "end_date": "2025-09-30",
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum"
    ],
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)

dados = response.json()

with open(
    "dados/clima_uberlandia.json",
    "w",
    encoding="utf-8"
) as arquivo:
    json.dump(
        dados,
        arquivo,
        ensure_ascii=False,
        indent=4
    )

print("JSON salvo com sucesso.")
