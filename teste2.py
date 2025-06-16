import requests
import json
urlDEX = 'https://api.dexscreener.com/latest/dex/pairs/base/0x3d5D143381916280ff91407FeBEB52f2b60f33Cf'
resposta_apiDEX = requests.get(urlDEX)
if resposta_apiDEX.status_code == 200:
    dados = resposta_apiDEX.json()
    print(json.dumps(dados, indent=4))
else:
    print('Erro API', resposta_apiDEX.status_code)