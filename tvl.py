import requests
from datetime import datetime, timezone, timedelta
# função personalizada criada p/ consulta do tvl atual
def tvl_aero():
    url_tvl_aero = 'https://api.llama.fi/tvl/aerodrome'
    resposta_tvl_aero = requests.get(url_tvl_aero)
    return resposta_tvl_aero.json()
aero_tvl = tvl_aero()
print(f"TVL atual da AERO: ${aero_tvl:,.2f}")
# função personalizada criada p/ consulta do tvl dos ultimos 30d
def tvl_30d():
    url_tvl30d = 'https://api.llama.fi/protocol/aerodrome-v1'
    resposta_tvl30d = requests.get(url_tvl30d)
    if resposta_tvl30d.status_code == 200:
        tvl30dias = resposta_tvl30d.json()
        timestamp_30d_exatos = int((datetime.now(timezone.utc) - timedelta(days=30)).timestamp())
        registro_ideal = None
        menor_diferenca = float('inf')
        for item in tvl30dias['tvl']:
            diferenca = abs(item['date'] - timestamp_30d_exatos)
            if diferenca < menor_diferenca:
                registro_ideal = item
        tvl_passado = registro_ideal['totalLiquidityUSD']
        data_passada = datetime.fromtimestamp(registro_ideal['date'], tz=timezone.utc).strftime('%d/%m/%Y')
        return tvl_passado, data_passada
    else:
        print('Erro ao acessar o historico de TVL. Codigo:', resposta_tvl30d.status_code)
        return None
tvl_30d_atras, data_passada = tvl_30d()
# logica condicional para analise do tvl
if tvl_30d_atras is not None:
    if tvl_30d_atras > aero_tvl:
        resultado = 'tvl diminuiu'
    elif tvl_30d_atras < aero_tvl:
        resultado = 'tvl aumentou'
    else:
        resultado = 'tvl estavel'
else: 
    resultado = 'Erro ao obter TVL de 30 dias atrás'
print(f'Resultado da análise de TVL de 30 dias atrás ({data_passada}) para data atual: {resultado}')