# importando biblioteca requests para acessar dados na internet
import requests
url = "https://coins.llama.fi/prices/current/base:0x940181a94A35A4569E4529A3CDfB74e38FD98631"
resposta = requests.get(url)
dados = resposta.json()
preco = dados['coins']['base:0x940181a94A35A4569E4529A3CDfB74e38FD98631']['price']
# analise de suporte vs resistencia usando logica condicional
if preco < 0.4924:
    analise = 'perca de suporte'
elif preco > 0.6215:
    analise = 'rompimento POC'
else:
    analise = 'lateralização'
# dicionário do token
token_aero = {
    'nome': 'AERO',
    'rede': 'Base',
    'preco': preco,
    'analise': analise
}
# dados historicos de volume (dex aerodrome finance) por meio da api defillama
url_volume = "https://api.llama.fi/summary/dexs/aerodrome"
resposta_volume = requests.get(url_volume)
dados_volume = resposta_volume.json()
volume_24h = dados_volume['total24h']
volume_7d = dados_volume['total7d']
# # cálculo manual do volume dos últimos 30 dias (não existe chave direta na API pra isso)
lista_diaria = dados_volume['totalDataChart']
ultimos_30d = lista_diaria[-30:]
soma_30d = 0
# lista_diaria percorrida utilizando estrutura de repetição for (loop-for)
for timestamp, volume in ultimos_30d:
    soma_30d += volume
# dicionário com volumes agregados 24h, 7d e 30d
volume_aero = {
    '24h': volume_24h,
    '7d': volume_7d,
    '30d': soma_30d
}
print(f'O token {token_aero['nome']} na rede {token_aero['rede']} está custando ${token_aero['preco']:.4f} e seu estado é de {token_aero['analise']}.')
print(f'Volume 24h: ${volume_aero['24h']}   Volume 7d: ${volume_aero['7d']}   Volume 30d: ${volume_aero['30d']}')