# importação de modulos e bibliotecas internas do python
import os
import json

# importação de modulos e bibliotecas externas do python
import requests
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta, timezone

# ajuste de caminho .env
dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

# função personalizada
def want33d():

    # ajuste de data/hora
    agora = datetime.now(timezone.utc)
    limite_24h = agora - timedelta(hours=24)

    # variavel que armazena minha chave api privada
    apiBASEscan_chavePrivada = os.getenv('BASESCAN_API_CHAVE')
    
    # dicionário json pool aero/eth | via api dexScrenner
    url_aeroeth = 'https://api.dexscreener.com/latest/dex/pairs/base/0x7f670f78B17dEC44d5Ef68a48740b6f8849cc2e6'
    resposta_aeroeth = requests.get(url_aeroeth)
    dicionario_aeroeth = resposta_aeroeth.json()

    url_eth = 'https://coins.llama.fi/prices/current/coingecko:ethereum'
    resposta_eth = requests.get(url_eth)
    dicionario_eth = resposta_eth.json()
        
    # captura de preço AERO e ETH
    preco_aeroeth = dicionario_aeroeth['pair']['priceUsd']
    preco_eth = dicionario_eth['coins']['coingecko:ethereum']['price']
        
    # captura de variacao de preço | 3 timestamps | 1h - 6h - 24h
    variacao_1h = dicionario_aeroeth['pair']['priceChange']['h1']
    variacao_6h = dicionario_aeroeth['pair']['priceChange']['h6']
    variacao_24h = dicionario_aeroeth['pair']['priceChange']['h24']
        
    # captura de volumes | 3 timestamps | 1h - 6h - 24h
    volume_1h = dicionario_aeroeth['pair']['volume']['h1']
    volume_6h = dicionario_aeroeth['pair']['volume']['h6']
    volume_24h = dicionario_aeroeth['pair']['volume']['h24']
        
    # captura de transações | 3 timestamps | 1h - 6h - 24h
    compras_1h = dicionario_aeroeth['pair']['txns']['h1']['buys']
    compras_6h = dicionario_aeroeth['pair']['txns']['h6']['buys']
    compras_24h = dicionario_aeroeth['pair']['txns']['h24']['buys']
    vendas_1h = dicionario_aeroeth['pair']['txns']['h1']['sells']
    vendas_6h = dicionario_aeroeth['pair']['txns']['h6']['sells']
    vendas_24h = dicionario_aeroeth['pair']['txns']['h24']['sells']
    
    # transações totais | 3 timestamps | 1h - 6h - 24h
    total_1h = compras_1h + vendas_1h
    total_6h = compras_6h + vendas_6h
    total_24h = compras_24h + vendas_24h
    
    # liquidez na pool 
    liquidez = dicionario_aeroeth['pair']['liquidity']['usd']
    
    # captura de marketcap (na lista 0)
    marketcap = dicionario_aeroeth['pairs'][0]['marketCap']

    return {
        'preco_usd': float(preco_aeroeth),
        'precoETH_usd': float(preco_eth),
        'variacao': {
            '1h': float(variacao_1h),
            '6h': float(variacao_6h),
            '24h': float(variacao_24h)
        },
        'volume': {
            '1h': float(volume_1h),
            '6h': float(volume_6h),
            '24h': float(volume_24h)
        },
        'transacoes': {
            'c1h': float(compras_1h),
            'c6h': float(compras_6h),
            'c24h': float(compras_24h),
            'v1h': float(vendas_1h),
            'v6h': float(vendas_6h),
            'v24h': float(vendas_24h)
        },
        'transacoesTotal': {
            't1h': float(total_1h),
            't6h': float(total_6h),
            't24h': float(total_24h)
        },
        'liquidez_usd': float(liquidez),
        'marketCap': float(marketcap)
    }
if __name__ == '__main__':
    want33d()