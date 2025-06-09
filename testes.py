import requests
# função personalizada criada p/ consulta do tvl atual
def tvl_aero():
    url_tvl_aero = 'https://api.llama.fi/tvl/aerodrome'
    resposta_tvl_aero = requests.get(url_tvl_aero)
    return resposta_tvl_aero.json()
aero_tvl = tvl_aero()
print(f"TVL atual da AERO: ${aero_tvl:,.2f}")
# função personalizada criada p/ consulta do tvl dos ultimos 30d
def tvl_30d():
    url_tvl30d = 'https://api.llama.fi/chart/protocol/aerodrome'
    resposta_tvl30d = requests.get(url_tvl30d)
    if resposta_tvl30d.status_code == 200:
        tvl30dias = resposta_tvl30d.json()
        tvl_passado = tvl30dias[-31]['tvl']
        return tvl_passado
    else:
        print('Erro ao acessar o historico de TVL. Codigo:', resposta_tvl30d.status_code)
        return None
tvl_30d_atras = tvl_30d()
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
print(f'Resultado da análise de TVL: {resultado}')